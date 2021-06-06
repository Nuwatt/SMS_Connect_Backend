from django.db.models import Count, Max, Min, Avg, OuterRef, Subquery, Q, F
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.localize.models import City
from apps.product.models import SKU
from apps.response.models import NumericAnswer, ChoiceAnswer


class SKUOverallReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            available=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Available')
            ) / F('total_answer') * 100,
            not_available=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
            less=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than 6')
            ) / F('total_answer') * 100,
        ).values(
            'available',
            'name',
            'not_available',
            'less'
        )


class SKUMonthAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Available')
            ) / F('total_answer') * 100,
        ).values(
            'month',
            'value',
            'name',
        )


class SKUMonthNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
        ).values(
            'month',
            'value',
            'name',
        )


class SKUMonthLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than 6')
            ) / F('total_answer') * 100,
        ).values(
            'month',
            'value',
            'name',
        )


class SKUCityAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            city=F('question__answer__response__store__city__name'),
        ).values('name', 'city').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Available')
            ) / F('total_answer') * 100,
        ).values(
            'city',
            'value',
            'name',
        )


class SKUCityNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            city=F('question__answer__response__store__city__name'),
        ).values('name', 'city').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Not Available')
            ) / F('total_answer') * 100,
        ).values(
            'city',
            'value',
            'name',
        )


class SKUCityLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            city=F('question__answer__response__store__city__name'),
        ).values('name', 'city').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than 6')
            ) / F('total_answer') * 100,
        ).values(
            'city',
            'value',
            'name',
        )


class SKUStoreLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            store=F('question__answer__response__store__name'),
        ).values('name', 'store').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than 6')
            ) / F('total_answer') * 100,
        ).values(
            'store',
            'value',
            'name',
        )


class SKURetailerLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock'
        ).annotate(
            retailer=F('question__answer__response__store__retailer__name'),
        ).values('name', 'retailer').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than 6')
            ) / F('total_answer') * 100,
        ).values(
            'retailer',
            'value',
            'name',
        )


class TotalVisitReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = City.objects.annotate(
            value=Count(
                'store__response',
                filter=Q(
                    store__response__questionnaire__questionnaire_type__name='Out Of Stock',
                )
            ),
        ).values('name', 'value',).filter(value__gt=0)
