from django.db.models import Count, Max, Min, Avg, OuterRef, Subquery, F, Q
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.localize.models import City
from apps.product.models import SKU, Brand
from apps.response.models import NumericAnswer


class SKUMinMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question=OuterRef('question'),
        ).annotate(
            frequency=Count('numeric')
        ).order_by(
            '-frequency'
        ).values('numeric')[:1]

        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).annotate(
            max=Max('question__answer__numericanswer__numeric'),
            min=Min('question__answer__numericanswer__numeric'),
            mean=Avg('question__answer__numericanswer__numeric'),
            mode=Subquery(numeric_answer)
        ).unarchived()


class SKUMonthMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True,
        ).values('name').annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            value=Max('question__answer__numericanswer__numeric'),
        ).values(
            'month',
            'value',
            'name',
        ).unarchived()


class SKUMonthMinReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            value=Min('question__answer__numericanswer__numeric'),
        ).values(
            'month',
            'value',
            'name',
        ).unarchived()


class SKUMonthMeanReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            value=Avg('question__answer__numericanswer__numeric'),
        ).values(
            'month',
            'value',
            'name',
        ).unarchived()


class SKUMonthModeReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question=OuterRef('question'),
        ).annotate(
            frequency=Count('numeric')
        ).order_by(
            '-frequency'
        ).values('numeric')[:1]

        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('month').distinct().annotate(
            value=Subquery(numeric_answer),
        ).values(
            'month',
            'value',
            'name',
        ).unarchived()


class SKUCountryMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            country=F('question__answer__response__store__city__country__name'),
        ).values('name', 'country').annotate(
            value=Max('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'value',
            'name',
        ).unarchived()


class SKUCountryMinReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            country=F('question__answer__response__store__city__country__name'),
        ).values('name', 'country').annotate(
            value=Min('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'value',
            'name',
        ).unarchived()


class SKUCountryMeanReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            country=F('question__answer__response__store__city__country__name'),
        ).values('name', 'country').annotate(
            value=Avg('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'value',
            'name',
        ).unarchived()


class SKUCountryModeReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question=OuterRef('question'),
        ).annotate(
            frequency=Count('numeric')
        ).order_by(
            '-frequency'
        ).values('numeric')[:1]

        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).annotate(
            country=F('question__answer__response__store__city__country__name'),
        ).values(
            'country',
        ).distinct().annotate(
            value=Subquery(numeric_answer),
        ).values(
            'country',
            'name',
            'value'
        ).unarchived()


class AnswerPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            country=F('question__answer__response__store__city__country__name'),
        ).values('name', 'country').annotate(
            value=Count('question__answer__response'),
        ).values(
            'country',
            'value',
            'name',
        ).unarchived()


class AnswerPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('name').annotate(
            city=F('question__answer__response__store__city__name'),
        ).values('name', 'city').annotate(
            value=Count('question__answer__response'),
        ).values(
            'city',
            'value',
            'name',
        ).unarchived()


class AnswerPerSKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.annotate(
            value=Count(
                'question__answer__response',
            )
        ).values('name', 'value').unarchived()


class TotalVisitReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = City.objects.annotate(
            value=Count(
                'store__response',
                filter=Q(
                    store__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
                )
            )
        ).values('name', 'value').filter(value__gt=0).unarchived()


class BrandMinMaxReportReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question__sku__brand=OuterRef('id'),
        ).annotate(
            frequency=Count('numeric')
        ).order_by(
            '-frequency'
        ).values('numeric')[:1]

        self._results = Brand.objects.filter(
            sku__question__questionnaire__questionnaire_type__name='Price Monitor',
            sku__question__answer__response__is_completed=True
        ).annotate(
            max=Max('sku__question__answer__numericanswer__numeric'),
            min=Min('sku__question__answer__numericanswer__numeric'),
            mean=Avg('sku__question__answer__numericanswer__numeric'),
            mode=Subquery(numeric_answer)
        ).unarchived()
