from django.db.models import Count, Q, F
from django.db.models.functions import TruncMonth, TruncWeek, ExtractWeek
from django.utils.timezone import now

from apps.core import usecases
from apps.localize.models import City
from apps.product.models import SKU


class SKUOverallReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
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
                filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
        ).values(
            'available',
            'name',
            'not_available',
            'less'
        ).unarchived()


class SKUMonthAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
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
        ).unarchived()


class SKUMonthNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
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
        ).unarchived()


class SKUMonthLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
        ).annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
        ).values(
            'month',
            'value',
            'name',
        ).unarchived()


class SKUCityAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
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
        ).unarchived()


class SKUCityNotAvailableReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
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
        ).unarchived()


class SKUCityLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
        ).annotate(
            city=F('question__answer__response__store__city__name'),
        ).values('name', 'city').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
        ).values(
            'city',
            'value',
            'name',
        ).unarchived()


class SKUStoreLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
        ).annotate(
            store=F('question__answer__response__store__name'),
        ).values('name', 'store').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
        ).values(
            'store',
            'value',
            'name',
        ).unarchived()


class SKURetailerLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True
        ).annotate(
            retailer=F('question__answer__response__store__retailer__name'),
        ).values('name', 'retailer').annotate(
            total_answer=Count('question__answer__choiceanswer__choice'),
            value=Count(
                'question__answer__choiceanswer__choice',
                filter=Q(question__answer__choiceanswer__choice__choice='Less than six (<6)')
            ) / F('total_answer') * 100,
        ).values(
            'retailer',
            'value',
            'name',
        ).unarchived()


class TotalVisitReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = City.objects.annotate(
            value=Count(
                'store__response',
                filter=Q(
                    store__response__response_cycle__questionnaire__questionnaire_type__name='Out Of Stock',
                )
            ),
        ).values('name', 'value', ).filter(value__gt=0).unarchived()


class SKUWeekLessReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        current_week = now().isocalendar()[1]
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Out Of Stock',
            question__answer__response__is_completed=True,
            question__answer__choiceanswer__choice__choice='Less than six (<6)'
        ).annotate(
            completed_week=ExtractWeek('question__answer__response__completed_at'),
            week=current_week - F('completed_week')
        ).values(
            'name',
            'week',
            'question__answer__response__store__name',
            'question__answer__response__store__retailer__name',
        ).filter(week__lte=4)
