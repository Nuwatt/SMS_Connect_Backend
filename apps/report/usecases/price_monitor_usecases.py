from django.db.models import Count, Max, Min, Avg, OuterRef, Subquery, F
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.response.models import NumericAnswer, Response


class SKUMinMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question__sku=OuterRef('answer__question__sku'),
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
        ).values(
            'numeric',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('numeric')[:1]

        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            max=Max('numeric'),
            min=Min('numeric'),
            mean=Avg('numeric'),
            mode=Subquery(numeric_answer)
        ).values(
            'max',
            'min',
            'mean',
            'mode',
            'sku_name',
        )


class SKUMonthMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            month=TruncMonth('answer__response__completed_at'),
        ).values(
            'month',
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            value=Max('numeric')
        ).values(
            'value',
            'month',
            'sku_name',
        )


class SKUMonthMinReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            month=TruncMonth('answer__response__completed_at'),
        ).values(
            'month',
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            value=Min('numeric')
        ).values(
            'value',
            'month',
            'sku_name',
        )


class SKUMonthMeanReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            month=TruncMonth('answer__response__completed_at'),
        ).values(
            'month',
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            value=Avg('numeric')
        ).values(
            'value',
            'month',
            'sku_name',
        )


class SKUMonthModeReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question__sku=OuterRef('answer__question__sku'),
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
        ).values(
            'numeric',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('numeric')[:1]

        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        ).annotate(
            month=TruncMonth('answer__response__completed_at'),
        ).values(
            'month',
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            value=Subquery(numeric_answer)
        ).values(
            'value',
            'month',
            'sku_name',
        )


class SKUCountryMaxReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            country=F('answer__response__store__city__country')
        ).values(
            'country'
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            country_name=F('answer__response__store__city__country__name'),
            value=Max('numeric')
        ).values(
            'value',
            'sku_name',
            'country_name'
        )


class SKUCountryMinReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            country=F('answer__response__store__city__country')
        ).values(
            'country'
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            country_name=F('answer__response__store__city__country__name'),
            value=Min('numeric')
        ).values(
            'value',
            'sku_name',
            'country_name'
        )


class SKUCountryMeanReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            country=F('answer__response__store__city__country')
        ).values(
            'country'
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            country_name=F('answer__response__store__city__country__name'),
            value=Avg('numeric')
        ).values(
            'value',
            'sku_name',
            'country_name'
        )


class SKUCountryModeReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question__sku=OuterRef('answer__question__sku'),
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__store__city__country=OuterRef('store__city__country')
        ).values(
            'numeric',
        ).order_by(
            'created',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('numeric')[:1]

        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            country=F('answer__response__store__city__country')
        ).values(
            'country'
        ).annotate(
            sku_name=F('answer__question__sku__name'),
            country_name=F('answer__response__store__city__country__name'),
            value=Subquery(numeric_answer)
        ).values(
            'value',
            'sku_name',
            'country_name'
        )


class AnswerPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            is_completed=True
        ).annotate(
            country=F('store__city__country')
        ).values(
            'country'
        ).annotate(
            country_name=F('store__city__country__name'),
            value=Count(
                'id',
            )
        ).values('country_name', 'value').filter(value__gt=0).unarchived()


class AnswerPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
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


class AnswerPerSKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        )


class BrandMinMaxReportReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        numeric_answer = NumericAnswer.objects.filter(
            answer__question__sku__brand=OuterRef('answer__question__sku__brand')
        ).values(
            'numeric',
        ).annotate(
            frequency=Count('id')
        ).order_by(
            '-frequency',
        ).values('numeric')[:1]

        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Price Monitor',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            brand=F('answer__question__sku__brand')
        ).values(
            'brand'
        ).annotate(
            brand_name=F('answer__question__sku__brand__name'),
            max=Max('numeric'),
            min=Min('numeric'),
            mean=Avg('numeric'),
            mode=Subquery(numeric_answer)
        ).values(
            'max',
            'min',
            'mean',
            'mode',
            'brand_name'
        )
