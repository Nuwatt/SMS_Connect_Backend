from django.db.models import Sum, F

from apps.report.filtersets.base_filtersets import (
    ResponseFilter,
    SKUResponseFilter,
    NumericAnswerReportFilter, ChoiceAnswerFilter
)
from apps.report.serializers import distribution_check_serializers
from apps.report.usecases import distribution_check_usecases
from apps.report.views.base_views import BaseReportView


class VisitPerCountryReportView(BaseReportView):
    """
    Use this end-point to list report of visit per country for distribution check
    """
    serializer_class = distribution_check_serializers.VisitPerCountryReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.VisitPerCountryReportUseCase().execute()


# optimized
class VisitPerCityReportView(BaseReportView):
    """
    Use this end-point to list report of visit per city for distribution check
    """
    serializer_class = distribution_check_serializers.VisitPerCityReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.VisitPerCityReportUseCase().execute()


# optimized
class VisitPerChannelReportView(BaseReportView):
    """
    Use this end-point to list report of visit per channel for distribution check
    """
    serializer_class = distribution_check_serializers.VisitPerChannelReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.VisitPerChannelReportUseCase().execute()


class SKUPerCityReportView(BaseReportView):
    """
    Use this end-point to list report of total sku per city for distribution check
    """
    serializer_class = distribution_check_serializers.SKUPerCityReportSerializer
    filterset_class = ChoiceAnswerFilter

    def get_queryset(self):
        return distribution_check_usecases.SKUPerCityReportUseCase().execute()


class SKUPerCountryReportView(BaseReportView):
    """
    Use this end-point to list report of total sku per country for distribution check
    """
    serializer_class = distribution_check_serializers.SKUPerCountryReportSerializer
    filterset_class = ChoiceAnswerFilter

    def get_queryset(self):
        return distribution_check_usecases.SKUPerCountryReportUseCase().execute()


class SKUPerChannelReportView(BaseReportView):
    """
    Use this end-point to list report of total sku per channel for distribution check
    """
    serializer_class = distribution_check_serializers.SKUPerChannelReportSerializer
    filterset_class = ChoiceAnswerFilter

    def get_queryset(self):
        return distribution_check_usecases.SKUPerChannelReportUseCase().execute()


class BrandPerCityReportView(BaseReportView):
    """
    Use this end-point to list report of total brand per city for distribution check
    """
    serializer_class = distribution_check_serializers.BrandPerCityReportSerializer
    filterset_class = ChoiceAnswerFilter

    def get_queryset(self):
        return distribution_check_usecases.BrandPerCityReportUseCase().execute()


class BrandPerCountryReportView(BaseReportView):
    """
    Use this end-point to list report of total brand per country for distribution check
    """
    serializer_class = distribution_check_serializers.BrandPerCountryReportSerializer
    filterset_class = ChoiceAnswerFilter

    def get_queryset(self):
        return distribution_check_usecases.BrandPerCountryReportUseCase().execute()


class BrandPerChannelReportView(BaseReportView):
    """
    Use this end-point to list report of total brand per channel for distribution check
    """
    serializer_class = distribution_check_serializers.BrandPerChannelReportSerializer
    filterset_class = ChoiceAnswerFilter

    def get_queryset(self):
        return distribution_check_usecases.BrandPerChannelReportUseCase().execute()


class AvgPerSKUReportView(BaseReportView):
    """
    Use this end-point to list report of avg per sku for distribution check
    """
    serializer_class = distribution_check_serializers.AvgPerSKUReportSerializer
    filterset_class = NumericAnswerReportFilter

    def get_queryset(self):
        return distribution_check_usecases.AvgPerSKUReportUseCase().execute()

    def custom_queryset(self, queryset):
        total_sum = queryset.aggregate(Sum('numeric')).get('numeric__sum')
        return queryset.annotate(
            sum_of_value=Sum('numeric'),
            value=F('sum_of_value') / total_sum * 100,
            sku_name=F('answer__question__sku__name'),
            brand=F('answer__question__sku__brand'),
        ).values(
            'value',
            'sku_name',
        )


class AvgPerBrandReportView(BaseReportView):
    """
    Use this end-point to list report of avg per brand for distribution check
    """
    serializer_class = distribution_check_serializers.AvgPerBrandReportSerializer
    filterset_class = NumericAnswerReportFilter

    def get_queryset(self):
        return distribution_check_usecases.AvgPerBrandReportUseCase().execute()

    def custom_queryset(self, queryset):
        total_sum = queryset.aggregate(Sum('numeric')).get('numeric__sum')
        return queryset.annotate(
            sum_of_value=Sum('numeric'),
            value=F('sum_of_value') / total_sum * 100,
            brand_name=F('answer__question__sku__brand__name'),
        ).values(
            'brand',
            'value',
            'brand_name'
        )


class AvgPerChannelReportView(BaseReportView):
    """
    Use this end-point to list report of avg per channel for distribution check
    """
    serializer_class = distribution_check_serializers.AvgPerChannelReportSerializer
    filterset_class = NumericAnswerReportFilter

    def get_queryset(self):
        return distribution_check_usecases.AvgPerChannelReportUseCase().execute()

    def custom_queryset(self, queryset):
        total_sum = queryset.aggregate(Sum('numeric')).get('numeric__sum')
        return queryset.annotate(
            sum_of_value=Sum('numeric'),
            value=F('sum_of_value') / total_sum * 100,
            channel_name=F('answer__response__store__channel__name'),
        ).values(
            'channel',
            'value',
            'channel_name'
        )
