from datetime import timedelta

from django.db.models import Q, Count, Subquery, OuterRef
from sql_util.aggregates import SubqueryCount

from apps.core import usecases
from apps.market.models import Store
from apps.question.models import Question
from apps.questionnaire.exceptions import QuestionnaireNotFound
from apps.questionnaire.models import Questionnaire
from apps.response.models import ResponseCycle
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

    def _factory(self):
        if 'repeat_cycle' in self._data:
            self._data['repeat_cycle'] = timedelta(weeks=self._data.get('repeat_cycle'))

        super(UpdateQuestionnaireUseCase, self)._factory()


class DeleteQuestionnaireUseCase(usecases.DeleteUseCase):
    def __init__(self, questionnaire: Questionnaire):
        super().__init__(questionnaire)


class ListQuestionnaireUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._questionnaires

    def _factory(self):
        self._questionnaires = Questionnaire.objects.unarchived().prefetch_related(
            'city__country',
            'tags__user'
        ).select_related(
            'questionnaire_type',
            'category',
        ).annotate(
            number_of_questions=Count('question')
        )


class ListAvailableQuestionnaireForAgentUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser):
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._questionnaires

    def _factory(self):
        agent_operation_cities = self._agent_user.operation_city.all()

        # 1. check incomplete response cycle
        completed_questionnaire = self._agent_user.responsecycle_set.filter(
            is_completed=True
        ).values_list('questionnaire', flat=True)

        self._questionnaires = self._questionnaires = Questionnaire.objects.unarchived().exclude(
            id__in=completed_questionnaire
        ).filter(
            Q(city__in=agent_operation_cities) |
            Q(tags__in=[self._agent_user])
        ).values('id').distinct().annotate(
            number_of_questions=SubqueryCount(
                'question',
                filter=Q(is_archived=False)
            ),
        ).values(
            'id',
            'number_of_questions',
            'name',
            'questionnaire_type__name',
            'created',
        ).filter(
            number_of_questions__gt=0
        )
        # ).values(
        #     'id',
        #     'name',
        #     # 'questionnaire_type__name',
        #     # 'created',
        # )

        # for item in self._questionnaires:
        #     print(item.id, item.number_of_questions)
        #     # print(item.question_set.count())
        # print('-'*10)
        # self._questionnaires = Questionnaire.objects.unarchived().select_related(
        #     'questionnaire_type'
        # ).annotate(
        #     number_of_questions=Count('question')
        # ).filter(
        #     Q(city__in=self._agent_user.operation_city.all()) |
        #     Q(tags__in=[self._agent_user])
        # ).distinct().annotate(
        #     eligible=Case(
        #         When(
        #             response=None,
        #             then=True
        #         ),
        #         When(
        #             response__agent=self._agent_user,
        #             response__is_completed=False,
        #             then=True
        #         ),
        #         When(
        #             response__agent=self._agent_user,
        #             response__is_completed=True,
        #             response__completed_at__gte=now() - F('repeat_cycle'),
        #             can_repeat=True,
        #             then=True
        #         ),
        #         default=False,
        #         output_field=models.BooleanField()
        #     ),
        # ).filter(
        #     eligible=True
        # )


class ListCompletedQuestionnaireStoresForAgentUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user: AgentUser, questionnaire: Questionnaire):
        self._questionnaire = questionnaire
        self._agent_user = agent_user

    def execute(self):
        self._factory()
        return self._stores

    def _factory(self):
        try:
            latest_response_cycle = self._agent_user.responsecycle_set.get(
                questionnaire=self._questionnaire,
                is_completed=False
            )
            self._stores = latest_response_cycle.response_set.filter(
                is_completed=True
            ).values('store_id', 'store__name')
        except ResponseCycle.DoesNotExist:
            self._stores = Store.objects.none()
