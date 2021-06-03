from datetime import timedelta

from django.db import models
from django.db.models import Q, Subquery, Case, When, F
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.questionnaire.exceptions import QuestionnaireNotFound
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
        tags = self._data.pop('tags', None)
        repeat_cycle = self._data.pop('repeat_cycle', None)

        # 2. create questionnaire
        self._questionnaire = Questionnaire.objects.create(**self._data)

        # 3. set city and country and tags
        self._questionnaire.city.set(city)
        if tags:
            self._questionnaire.tags.set(tags)

        # 4. repeat cycle
        if repeat_cycle:
            self._questionnaire.repeat_cycle = timedelta(weeks=repeat_cycle)
            self._questionnaire.save()


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
            'city__country'
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
        self._questionnaires = Questionnaire.objects.unarchived().select_related(
            'questionnaire_type'
        ).annotate(
            eligible=Case(
                When(
                    response__agent=self._agent_user,
                    response__completed_at__gte=now() - F('repeat_cycle'),
                    can_repeat=True,
                    then=True
                ),
                When(
                    response=None,
                    then=True
                ),
                When(
                    response__agent=self._agent_user,
                    response__is_completed=False,
                    then=True
                ),
                default=False,
                output_field=models.BooleanField()
            ),
        ).filter(
            eligible=True
        ).filter(
            Q(city__in=self._agent_user.operation_city.all()) |
            Q(tags__in=[self._agent_user])
        ).distinct()
