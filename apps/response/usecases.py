from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.questionnaire.models import Questionnaire
from apps.response.exceptions import ResponseNotFound
from apps.response.models import Response, Answer, ChoiceAnswer, OptionAnswer, ImageAnswer, InputAnswer
from apps.user.models import AgentUser


class GetResponseUseCase(usecases.BaseUseCase):
    def __init__(self, response_id: str):
        self._response_id = response_id

    def execute(self):
        self._factory()
        return self._response

    def _factory(self):
        try:
            self._response = Response.objects.get(pk=self._response_id)
        except Response.DoesNotExist:
            raise ResponseNotFound


class StartQuestionnaireUseCase(usecases.CreateUseCase):
    def __init__(self, serializer, agent_user: AgentUser, questionnaire: Questionnaire):
        super().__init__(serializer)
        self._questionnaire = questionnaire
        self._agent_user = agent_user

    def execute(self):
        super(StartQuestionnaireUseCase, self).execute()
        return self._response

    def _factory(self):
        self._response = Response(
            agent=self._agent_user,
            questionnaire=self._questionnaire,
            **self._data
        )
        try:
            self._response.full_clean(exclude=['completed_date_time'])
            self._response.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


class SummitQuestionnaireResponseUseCase(usecases.CreateUseCase):
    def __init__(self, response: Response, serializer):
        super().__init__(serializer)
        self._response = response

    def _factory(self):
        for data in self._data.get('data'):
            question_type = data.get('question').question_type
            answer = Answer.objects.create(
                response=self._response,
                question=data.get('question')
            )
            if question_type.has_default_choices:
                ChoiceAnswer.objects.create(answer=answer, choice=data.get('choice_answer'))
            elif question_type.has_options:
                for option in data.get('option_answer'):
                    OptionAnswer.objects.create(answer=answer, option=option)
            elif question_type.name == 'Pictures':
                for picture in data.get('picture_answer'):
                    ImageAnswer.objects.create(answer=answer, image=picture)
            else:
                InputAnswer.objects.create(answer=answer, body=data.get('text_answer'))

        self._response.is_completed = True
        self._response.completed_date_time = now()
        self._response.save()

    def is_valid(self):
        # 1. check if response is completed.
        if self._response.is_completed:
            raise ValidationError({
                'non_field_errors': _('Requesting questionnaire is already completed.')
            })


class ListQuestionnaireResponseUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser):
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._responses

    def _factory(self):
        self._responses = self._agent_user.response_set.unarchived().select_related(
            'questionnaire',
            'questionnaire__questionnaire_type'
        )
