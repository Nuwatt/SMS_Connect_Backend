from django.db.models import Count, Q, F
from django.db.models.functions import TruncMonth, ExtractWeek, TruncWeek
from django.utils.timezone import now

from apps.core import usecases
from apps.response.models import Response, ChoiceAnswer


class SKUOverallReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            total_answer=Count('choice'),
            available=Count(
                'choice',
                filter=Q(choice__choice='Available')
            ) / F('total_answer') * 100,
            not_available=Count(
                'choice',
                filter=Q(choice__choice='Not Available')
            ) / F('total_answer') * 100,
            less=Count(
                'choice',
                filter=Q(choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
        ).values(
            'available',
            'not_available',
            'less',
            'sku_name',
        )


class SKUMonthAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            month=TruncMonth('answer__response__completed_at')
        ).values(
            'month'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'month',
            'sku_name',
        )


class SKUMonthNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            month=TruncMonth('answer__response__completed_at')
        ).values(
            'month'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Not Available')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'month',
            'sku_name',
        )


class SKUMonthLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            month=TruncMonth('answer__response__completed_at')
        ).values(
            'month'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'month',
            'sku_name'
        )


class SKUCityAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            city=F('answer__response__store__city')
        ).values(
            'city'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Available')
            ) / F('total_answer') * 100,
            city_name=F('answer__response__store__city__name'),
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'sku_name',
            'city_name'
        )


class SKUCityNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            city=F('answer__response__store__city')
        ).values(
            'city'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Not Available')
            ) / F('total_answer') * 100,
            city_name=F('answer__response__store__city__name'),
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'sku_name',
            'city_name'
        )


class SKUCityLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            city=F('answer__response__store__city')
        ).values(
            'city'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
            city_name=F('answer__response__store__city__name'),
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'sku_name',
            'city_name'
        )


class SKUStoreNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            retailer=F('answer__response__store__retailer')
        ).values(
            'retailer'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Not Available')
            ) / F('total_answer') * 100,
            store_name=F('answer__response__store__retailer__name'),
            sku_name=F('answer__question__sku__name'),
        ).values(
            'value',
            'sku_name',
            'store_name'
        )


class TotalVisitReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__question__question_type__name='OOS Question',
            is_completed=True
        ).annotate(
            city_name=F('store__city__name')
        ).values(
            'city_name'
        ).annotate(
            value=Count(
                'id',
                distinct=True
            )
        ).values('city_name', 'value').filter(value__gt=0).unarchived()


class SKUWeekNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        # current_week = now().isocalendar()[1]
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
            answer__response__is_completed=True,
            choice__choice='Not Available',
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            completed_week=TruncWeek('answer__response__completed_at'),
            # week=current_week - F('completed_week'),
            sku_name=F('answer__question__sku__name'),
            store_name=F('answer__response__store__name'),
            retailer_name=F('answer__response__store__retailer__name'),
        ).values(
            'completed_week',
            'sku_name',
            'store_name',
            'retailer_name'
        )
        # print(self._results)

