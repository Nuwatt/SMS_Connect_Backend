from django.db.models import Count, Max, Min, Avg, OuterRef, Subquery, F, Q
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.localize.models import City, Country
from apps.product.models import SKU
from apps.response.models import NumericAnswer


class SKUMinMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question__sku=OuterRef('id'),
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
        ).unarchived().filter(max__isnull=False)


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
        ).unarchived().filter(value__isnull=False)


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
        ).unarchived().filter(value__isnull=False)


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
        ).unarchived().filter(value__isnull=False)


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
        ).unarchived().filter(value__isnull=False)


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
            country_id=F('question__answer__response__store__city__country'),
            value=Max('question__answer__numericanswer__numeric'),
        ).values(
            'country',
            'country_id',
            'value',
            'name',
        ).unarchived().filter(value__isnull=False)


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
            country_id=F('question__answer__response__store__city__country'),
        ).values(
            'country',
            'country_id',
            'value',
            'name',
        ).unarchived().filter(value__isnull=False)


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
            country_id=F('question__answer__response__store__city__country'),
        ).values(
            'country',
            'country_id',
            'value',
            'name',
        ).unarchived().filter(value__isnull=False)


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
            country_id=F('question__answer__response__store__city__country'),
        ).values(
            'country',
            'country_id',
            'name',
            'value'
        ).unarchived().filter(value__isnull=False)


class AnswerPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Country.objects.annotate(
            value=Count(
                'city__store__response',
                filter=Q(
                    city__store__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
                ),
                distinct=True
            )
        ).values('name', 'value').filter(value__gt=0).unarchived()


class AnswerPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = City.objects.annotate(
            value=Count(
                'store__response',
                filter=Q(
                    store__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
                ),
                distinct=True
            )
        ).values('name', 'value').filter(value__gt=0).unarchived()
    # def execute(self):
    #     self._factory()
    #     return self._results
    #
    # def _factory(self):
    #     self._results = SKU.objects.filter(
    #         question__questionnaire__questionnaire_type__name='Price Monitor',
    #         question__answer__response__is_completed=True
    #     ).values('name').annotate(
    #         city=F('question__answer__response__store__city__name'),
    #     ).values('name', 'city').annotate(
    #         value=Count('question__answer__response'),
    #     ).values(
    #         'city',
    #         'value',
    #         'name',
    #     ).unarchived()


class AnswerPerSKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = SKU.objects.annotate(
            value=Count(
                'question__answer__response',
            )
        ).values('name', 'value').filter(value__gt=0).unarchived()


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
            answer__question__sku__brand=OuterRef('brand'),
        ).annotate(
            frequency=Count('numeric')
        ).order_by(
            '-frequency'
        ).values('numeric')[:1]

        self._results = SKU.objects.filter(
            question__questionnaire__questionnaire_type__name='Price Monitor',
            question__answer__response__is_completed=True
        ).values('brand').distinct().annotate(
            max=Max('question__answer__numericanswer__numeric'),
            min=Min('question__answer__numericanswer__numeric'),
            mean=Avg('question__answer__numericanswer__numeric'),
            mode=Subquery(numeric_answer)
        ).unarchived().filter(max__isnull=False).values(
            'max',
            'min',
            'mean',
            'mode',
            'brand__name',
            'brand',
        )
