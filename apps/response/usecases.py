from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction, IntegrityError
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.questionnaire.models import Questionnaire
from apps.response.exceptions import ResponseNotFound
from apps.response.models import (
    Response,
    Answer,
    ChoiceAnswer,
    OptionAnswer,
    ImageAnswer,
    TextAnswer,
    NumericAnswer, ResponseCycle
)
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
        # 1. get response cycle
        response_cycle, created = ResponseCycle.objects.get_or_create(
            agent=self._agent_user,
            questionnaire=self._questionnaire,
            is_completed=False
        )

        # 2. get response
        try:
            self._response, created = Response.objects.get_or_create(
                response_cycle=response_cycle,
                store=self._data.pop('store'),
                is_completed=False,
                defaults=self._data
            )
            self._response.created = now()
            self._response.save()
        except IntegrityError:
            raise ValidationError({
                'store': _('Agent has already submitted questionnaire for this store.')
            })

        # try:
        #     self._response = Response.objects.get(
        #         agent=self._agent_user,
        #         questionnaire=self._questionnaire,
        #         store=self._data.get('store'),
        #         is_completed=False
        #     )
        #     self._response.latitude = self._data.get('latitude')
        #     self._response.longitude = self._data.get('longitude')
        #     self._response.created = now()
        #     self._response.save()
        # except Response.DoesNotExist:
        #     self._response = Response(
        #         agent=self._agent_user,
        #         questionnaire=self._questionnaire,
        #         store=self._data.get('store'),
        #         latitude=self._data.get('latitude'),
        #         longitude=self._data.get('longitude')
        #     )
        #     try:
        #         self._response.clean()
        #         self._response.save()
        #     except DjangoValidationError as e:
        #         raise ValidationError(e.message_dict)

    def is_valid(self):
        if self._agent_user not in self._questionnaire.tags.all():
            if self._data.get('store').city not in self._questionnaire.city.all():
                raise DjangoValidationError({
                    'store': _('Store is not associated with questionnaire.')
                })


class SummitQuestionnaireResponseUseCase(usecases.CreateUseCase):
    def __init__(self, response: Response, serializer):
        super().__init__(serializer)
        self._response = response

    @transaction.atomic()
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
            elif question_type.name.lower() == 'image':
                for picture in data.get('image_answer'):
                    ImageAnswer.objects.create(answer=answer, image=picture)
            elif question_type.name.lower() == 'text':
                TextAnswer.objects.create(answer=answer, text=data.get('text_answer'))
            elif question_type.name.lower() == 'numeric':
                NumericAnswer.objects.create(answer=answer, numeric=data.get('numeric_answer'))

        self._response.is_completed = True
        self._response.completed_at = now()
        self._response.save()

    def is_valid(self):
        # 1. check if response is completed.
        if self._response.is_completed:
            raise ValidationError({
                'non_field_errors': _('Requesting questionnaire is already completed.')
            })


class ListAgentResponseHistoryUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser):
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._responses

    def _factory(self):
        try:
            latest_response_cycle = self._agent_user.responsecycle_set.filter(
                is_completed=True,
                is_archived=False
            ).latest('completed_at')

            self._responses = latest_response_cycle.response_set.unarchived().select_related(
                'questionnaire',
                'questionnaire__questionnaire_type'
            ).filter(
                is_completed=True
            )
        except ResponseCycle.DoesNotExist:
            self._responses = []


class ListAgentResponseUseCase(ListAgentResponseHistoryUseCase):
    def _factory(self):
        try:
            latest_response_cycle = self._agent_user.responsecycle_set.filter(
                is_completed=True,
                is_archived=False
            ).latest('completed_at')

            self._responses = latest_response_cycle.response_set.unarchived().select_related(
                'questionnaire',
                'questionnaire__questionnaire_type',
                'store',
                'store__retailer__channel',
                'store__city',
                'store__city__country'
            )
        except ResponseCycle.DoesNotExist:
            self._responses = []


class ListQuestionnaireResponseUseCase(usecases.BaseUseCase):
    def __init__(self, questionnaire: Questionnaire):
        self._questionnaire = questionnaire

    def execute(self):
        self._factory()
        return self._responses

    def _factory(self):
        try:
            latest_response_cycle = self._questionnaire.responsecycle_set.filter(
                is_completed=True,
                is_archived=False
            ).latest('completed_at')

            self._responses = latest_response_cycle.response_set.filter(
                is_completed=True,
                is_archived=False,
            ).select_related(
                'store',
                'store__retailer__channel',
                'store__city',
                'store__city__country'
            ).prefetch_related(
                'answer_set'
            )

        except ResponseCycle.DoesNotExist:
            self._responses = []


class ListQuestionnaireAnswerUseCase(usecases.BaseUseCase):
    def __init__(self, questionnaire: Questionnaire, agent_user: AgentUser):
        self._agent_user = agent_user
        self._questionnaire = questionnaire

    def execute(self):
        self._factory()
        return self._answers

    def _factory(self):
        try:
            latest_response_cycle = self._agent_user.responsecycle_set.filter(
                questionnaire=self._questionnaire,
                is_completed=True,
                is_archived=False
            ).latest('completed_at')

            try:
                latest_response = latest_response_cycle.response_set.filter(
                    is_completed=True,
                    is_archived=False
                ).prefetch_related(
                    'answer_set'
                ).latest('completed_at')

                self._answers = latest_response.answer_set.select_related(
                    'question',
                    'question__question_type',
                    'numericanswer',
                    'textanswer',
                    'choiceanswer',
                ).prefetch_related(
                    'imageanswer_set',
                    'optionanswer_set'
                )
            except Response.DoesNotExist:
                self._answers = []
        except ResponseCycle.DoesNotExist:
            self._answers = []


        # self._answers = [
        #     {
        #         "question_id": "Q0003",
        #         "question_type": "Numeric",
        #         "question": "What is the price for Afia corn 1.5L?",
        #         "answer": [50.878]
        #     },
        #     {
        #         "question_id": "Q0005",
        #         "question_type": "Multiple options multiple selection",
        #         "question": "How is the quality of Afia corn 1.5L?",
        #         "answer": ["Good", "smooth"]
        #     },
        #     {
        #         "question_id": "Q0007",
        #         "question_type": "Multiple options single selection",
        #         "question": "How is the taste of Afia corn 1.5L?",
        #         "answer": ["Good"]
        #     },
        #     {
        #         "question_id": "Q0087",
        #         "question_type": "Rating 1 to 10",
        #         "question": "Rate the taste of Afia corn 1.5L?",
        #         "answer": ["Worst"]
        #     },
        #     {
        #         "question_id": "Q0887",
        #         "question_type": "Text",
        #         "question": "Opinion on of Afia corn 1.5L?",
        #         "answer": ["Worst product ever"]
        #     },
        #     {
        #         "question_id": "Q8887",
        #         "question_type": "Image",
        #         "question": "Opinion on of Afia corn 1.5L?",
        #         "answer": [
        #             "https://www.luluhypermarket.com/medias/1671735-01.jpg-1200Wx1200H?context=bWFzdGVyfGltYWdlc3wyMTk1Mzh8aW1hZ2UvanBlZ3xpbWFnZXMvaDQxL2gyNy9oMDAvOTQ2NDIyMzg1ODcxOC5qcGd8YmVlMDJiY2VmMzZiNGI3YzVhYTkwZWYwOTJhYzEwM2M1MjBmMmFlY2EyNTZiYTgxMDFmNDNjYWZhMDJhZTA2OQ",
        #             "https://aqsaalmadina.com/wp-content/uploads/2021/04/Afia-Corn-Oil-9Litre-104.00.jpg"
        #         ]
        #     }
        # ]
