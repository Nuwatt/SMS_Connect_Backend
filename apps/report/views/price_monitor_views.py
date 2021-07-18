from django.db import models
from django.db.models import Count, F, Value

from apps.report.filtersets import price_monitor_filtersets
from apps.report.filtersets.base_filtersets import (
    SKUResponseFilter,
    ResponseFilter,
    NumericAnswerReportFilter
)
from apps.report.filtersets.price_monitor_filtersets import AnswerPerSKUFilter
from apps.report.serializers import price_monitor_serializers
from apps.report.usecases import price_monitor_usecases

# optimized
from apps.report.views.base_views import BaseReportView


class SKUMinMaxReportView(BaseReportView):
    """
    Use this end-point to list report of all sku min max for price monitor
    """
    serializer_class = price_monitor_serializers.SKUMinMaxReportSerializer
    filterset_class = NumericAnswerReportFilter

    def get_queryset(self):
        return price_monitor_usecases.SKUMinMaxReportUseCase().execute()


class SKUMonthReportView(BaseReportView):
    """
    Common SKU Month
    """

    serializer_class = price_monitor_serializers.SKUMonthReportSerializer
    filterset_class = NumericAnswerReportFilter


# optimized
class SKUMonthMaxReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku max vs month for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUMonthMaxReportUseCase().execute()


# optimized
class SKUMonthMinReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku min vs month for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUMonthMinReportUseCase().execute()


# optimized
class SKUMonthMeanReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku mean vs month for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUMonthMeanReportUseCase().execute()


# optimized
class SKUMonthModeReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku mode vs month for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUMonthModeReportUseCase().execute()


class SKUCountryReportView(BaseReportView):
    """
    Common SKU Country Report
    """
    serializer_class = price_monitor_serializers.SKUCountryReportSerializer
    filterset_class = NumericAnswerReportFilter


# optimized
class SKUCountryMaxReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku max vs country for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUCountryMaxReportUseCase().execute()


# optimized
class SKUCountryMinReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku min vs country for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUCountryMinReportUseCase().execute()


# optimized
class SKUCountryMeanReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku mean vs country for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUCountryMeanReportUseCase().execute()


# not optimized
class SKUCountryModeReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku mode vs country for price monitor
    """

    def get_queryset(self):
        return price_monitor_usecases.SKUCountryModeReportUseCase().execute()


# optimized
class AnswerPerCountryReportView(BaseReportView):
    """
    Use this end-point to list report of answer per country for price monitor
    """
    serializer_class = price_monitor_serializers.AnswerPerCountryReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerCountryReportUseCase().execute()


# optimized
class AnswerPerCityReportView(BaseReportView):
    """
    Use this end-point to list report of answer per country for price monitor
    """
    serializer_class = price_monitor_serializers.AnswerPerCityReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerCityReportUseCase().execute()


# optimized
class AnswerPerSKUReportView(BaseReportView):
    """
    Use this end-point to list report of answer per sku for price monitor
    """
    serializer_class = price_monitor_serializers.AnswerPerSKUReportSerializer
    filterset_class = NumericAnswerReportFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerSKUReportUseCase().execute()

    def custom_queryset(self, queryset):
        total_count = queryset.aggregate(Count('id')).get('id__count')
        return queryset.annotate(
            sku_name=F('answer__question__sku__name'),
            sku_count=Count('id'),
            value=Count('id') / total_count * 100,
            total_count=Value(total_count, output_field=models.IntegerField())
        ).values(
            'value',
            'sku_name',
            'sku_count',
            'total_count',
        )


class BrandMinMaxReportView(BaseReportView):
    """
    Use this end-point to list report of brand vs min max for price monitor
    """
    serializer_class = price_monitor_serializers.BrandMinMaxReportSerializer
    filterset_class = NumericAnswerReportFilter

    def get_queryset(self):
        return price_monitor_usecases.BrandMinMaxReportReportUseCase().execute()
