from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.questionnaire.models import Questionnaire
from apps.response.exceptions import ResponseNotFound
from apps.response.models import Response
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

    def _factory(self):
        response = Response(
            agent=self._agent_user,
            questionnaire=self._questionnaire,
            **self._data
        )
        try:
            response.full_clean(exclude=['completed_date_time'])
            response.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)

