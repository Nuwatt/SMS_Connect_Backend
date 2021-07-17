from django.db.models import Count, F, Q

from apps.core import usecases
from apps.response.models import NumericAnswer, Response, ChoiceAnswer


class VisitPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            is_completed=True
        ).annotate(
            city=F('store__city')
        ).values(
            'city'
        ).annotate(
            city_name=F('store__city__name'),
            value=Count(
                'id',
                distinct=True
            )
        ).values('city_name', 'value').filter(value__gt=0).unarchived()


class VisitPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            is_completed=True
        ).annotate(
            country=F('store__city__country')
        ).values(
            'country'
        ).annotate(
            country_name=F('store__city__country__name'),
            value=Count(
                'id',
                distinct=True
            )
        ).values('country_name', 'value').filter(value__gt=0).unarchived()


class VisitPerChannelReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = Response.objects.filter(
            response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            is_completed=True
        ).annotate(
            channel=F('store__channel')
        ).values(
            'channel'
        ).annotate(
            channel_name=F('store__channel__name'),
            value=Count(
                'id',
                distinct=True
            )
        ).values('channel_name', 'value').filter(value__gt=0).unarchived()


class SKUPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
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
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            city_name=F('answer__response__store__city__name')
        ).values(
            'value',
            'city_name',
            'sku_name',
        )


class SKUPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            country=F('answer__response__store__city__country')
        ).values(
            'country'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            country_name=F('answer__response__store__city__country__name')
        ).values(
            'value',
            'country_name',
            'sku_name',
        )


class SKUPerChannelReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            channel=F('answer__response__store__channel')
        ).values(
            'channel'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            sku_name=F('answer__question__sku__name'),
            channel_name=F('answer__response__store__channel__name')
        ).values(
            'value',
            'channel_name',
            'sku_name',
        )


class BrandPerCityReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            city=F('answer__response__store__city')
        ).values(
            'city'
        ).annotate(
            brand=F('answer__question__sku__brand')
        ).values(
            'brand'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            brand_name=F('answer__question__sku__brand__name'),
            city_name=F('answer__response__store__city__name'),
        ).values(
            'value',
            'brand_name',
            'city_name',
        )


class BrandPerCountryReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            country=F('answer__response__store__city__country')
        ).values(
            'country'
        ).annotate(
            brand=F('answer__question__sku__brand')
        ).values(
            'brand'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            brand_name=F('answer__question__sku__brand__name'),
            country_name=F('answer__response__store__city__country__name'),
        ).values(
            'value',
            'brand_name',
            'country_name',
        )


class BrandPerChannelReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = ChoiceAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            channel=F('answer__response__store__channel')
        ).values(
            'channel'
        ).annotate(
            brand=F('answer__question__sku__brand')
        ).values(
            'brand'
        ).annotate(
            total_answer=Count('choice'),
            value=Count(
                'choice',
                filter=Q(choice__choice='Yes')
            ) / F('total_answer') * 100,
            brand_name=F('answer__question__sku__brand__name'),
            channel_name=F('answer__response__store__channel__name'),
        ).values(
            'value',
            'brand_name',
            'channel_name',
        )


class AvgPerSKUReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            sku=F('answer__question__sku')
        ).values(
            'sku'
        )


class AvgPerBrandReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            brand=F('answer__question__sku__brand')
        ).values(
            'brand'
        )


class AvgPerChannelReportUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._results

    def _factory(self):
        self._results = NumericAnswer.objects.filter(
            answer__response__response_cycle__questionnaire__questionnaire_type__name='Distribution Check',
            answer__response__is_completed=True,
            is_archived=False
        ).annotate(
            channel=F('answer__response__store__channel')
        ).values(
            'channel'
        )
