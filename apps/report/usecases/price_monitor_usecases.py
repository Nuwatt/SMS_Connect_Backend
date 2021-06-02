from django.db.models import Count, Max, Min, Avg, OuterRef, Subquery, F
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.localize.models import City
from apps.product.models import SKU
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
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).annotate(
            max=Max('question__answer__numericanswer__numeric'),
            min=Min('question__answer__numericanswer__numeric'),
            mean=Avg('question__answer__numericanswer__numeric'),
            mode=Subquery(numeric_answer)
        )


class SKUMonthMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            value=Max('question__answer__numericanswer__numeric'),
        ).values(
            'month',
            'value',
            'name',
        )


class SKUMonthMinReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            value=Min('question__answer__numericanswer__numeric'),
        ).values(
            'month',
            'value',
            'name',
        )


class SKUMonthMeanReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('name', 'month').annotate(
            value=Avg('question__answer__numericanswer__numeric'),
        ).values(
            'month',
            'value',
            'name',
        )


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
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).annotate(
            month=TruncMonth('question__answer__response__completed_at'),
        ).values('month').distinct().annotate(
            value=Subquery(numeric_answer),
        ).values(
            'month',
            'value',
            'name',
        )


class SKUCountryMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            country=F('question__answer__response__retailer__country__name'),
        ).values('name', 'country').annotate(
            value=Max('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'value',
            'name',
        )


class SKUCountryMinReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            country=F('question__answer__response__retailer__country__name'),
        ).values('name', 'country').annotate(
            value=Min('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'value',
            'name',
        )


class SKUCountryMeanReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            country=F('question__answer__response__retailer__country__name'),
        ).values('name', 'country').annotate(
            value=Avg('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'value',
            'name',
        )


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
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).annotate(
            country=F('question__answer__response__retailer__country__name'),
        ).values(
            'country',
        ).distinct().annotate(
            value=Subquery(numeric_answer),
        ).values(
            'country',
            'name',
            'value'
        )


class AnswerPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            country=F('question__answer__response__retailer__country__name'),
        ).values('name', 'country').annotate(
            value=Count('question__answer__response'),
        ).values(
            'country',
            'value',
            'name',
        )


class AnswerPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor'
        ).values('name').annotate(
            city=F('question__answer__response__retailer__city__name'),
        ).values('name', 'city').annotate(
            value=Count('question__answer__response'),
        ).values(
            'city',
            'value',
            'name',
        )


class AnswerPerSKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.annotate(
            value=Count('question__answer__response')
        ).values('name', 'value')


class TotalVisitReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = City.objects.annotate(
            value=Count('retailer__response')
        ).values('name', 'value').filter(value__gt=0)
