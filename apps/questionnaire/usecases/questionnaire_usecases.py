from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError

from apps.questionnaire.exceptions import QuestionnaireNotFound
from apps.core import usecases
from apps.questionnaire.models import Questionnaire
from apps.user.models import AgentUser


class GetQuestionnaireUseCase(usecases.BaseUseCase):
    def __init__(self, questionnaire_id: str):
        self._questionnaire_id = questionnaire_id

    def execute(self):
        self._factory()
        return self._questionnaire

    def _factory(self):
        try:
            self._questionnaire = Questionnaire.objects.get(pk=self._questionnaire_id)
        except Questionnaire.DoesNotExist:
            raise QuestionnaireNotFound


class AddQuestionnaireUseCase(usecases.CreateUseCase):

    def execute(self):
        self.is_valid()
        self._factory()
        return self._questionnaire

    def _factory(self):
        # 1. pop city and country and tags
        city = self._data.pop('city')
        country = self._data.pop('country')
        tags = self._data.pop('tags')

        # 2. create questionnaire
        self._questionnaire = Questionnaire.objects.create(**self._data)

        # 3. set city and country and tags
        self._questionnaire.city.set(city)
        self._questionnaire.country.set(country)
        self._questionnaire.tags.set(tags)

    def is_valid(self):
        countries = self._data.get('country', None)

        if countries and 'city' in self._data:
            for city in self._data.get('city'):
                if city.country not in countries:
                    raise ValidationError({
                        'city': _('City:{} not belongs to submitted country.'.format(
                            city
                        ))
                    })


class UpdateQuestionnaireUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, questionnaire: Questionnaire):
        super().__init__(serializer, questionnaire)


class DeleteQuestionnaireUseCase(usecases.DeleteUseCase):
    def __init__(self, questionnaire: Questionnaire):
        super().__init__(questionnaire)


class ListQuestionnaireUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._questionnaires

    def _factory(self):
        self._questionnaires = Questionnaire.objects.unarchived().prefetch_related(
            'city',
            'country'
        ).select_related(
            'questionnaire_type',
        )


class ListAvailableQuestionnaireForAgentUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser):
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._questionnaires

    def _factory(self):
        self._questionnaires = Questionnaire.objects.unarchived().filter(
            Q(city__in=self._agent_user.operation_city.all()) |
            Q(tags__in=[self._agent_user])
        ).distinct()

