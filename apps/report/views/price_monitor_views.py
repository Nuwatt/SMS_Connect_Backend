from apps.core import generics
from apps.report.filtersets import (
    SKUMinMaxFilter,
    AnswerPerSKUFilter,
    AnswerPerCityFilter,
    AnswerPerCountryFilter
)
from apps.report.queryset_handlers import (
    sku_min_max_queryset_handler,
    SKUCountryQuerysetHandler,
    SKUMonthQuerysetHandler
)
from apps.report.serializers import price_monitor_serializers
from apps.report.usecases import price_monitor_usecases


class SKUMinMaxReportView(generics.ListAPIView):
    """
    Use this end-point to list report of all sku min max for price monitor
    """
    serializer_class = price_monitor_serializers.SKUMinMaxReportSerializer
    filterset_class = SKUMinMaxFilter
    pagination_class = None

    def get_queryset(self):
        return price_monitor_usecases.SKUMinMaxReportUseCase().execute()

    def custom_queryset(self, queryset):
        return sku_min_max_queryset_handler(queryset)


class SKUMonthReportView(generics.ListAPIView):
    """
    Common Class for SKU Month
    """

    serializer_class = price_monitor_serializers.SKUMonthReportSerializer
    filterset_class = SKUMinMaxFilter
    pagination_class = None

    def get_queryset(self):
        return price_monitor_usecases.SKUMonthReportUseCase().execute()


class SKUMonthMaxReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku max vs month for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUMonthQuerysetHandler(queryset).max()


class SKUMonthMinReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku min vs month for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUMonthQuerysetHandler(queryset).min()


class SKUMonthMeanReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku mean vs month for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUMonthQuerysetHandler(queryset).mean()


class SKUMonthModeReportView(SKUMonthReportView):
    """
    Use this end-point to list report of all sku mode vs month for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUMonthQuerysetHandler(queryset).mode()


class SKUCountryReportView(generics.ListAPIView):
    """
    Common SKU Country Report
    """
    serializer_class = price_monitor_serializers.SKUCountryReportSerializer
    filterset_class = SKUMinMaxFilter
    pagination_class = None

    def get_queryset(self):
        return price_monitor_usecases.SKUCountryReportUseCase().execute()


class SKUCountryMaxReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku max vs country for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUCountryQuerysetHandler(queryset).max()


class SKUCountryMinReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku min vs country for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUCountryQuerysetHandler(queryset).min()


class SKUCountryMeanReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku mean vs country for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUCountryQuerysetHandler(queryset).mean()


class SKUCountryModeReportView(SKUCountryReportView):
    """
    Use this end-point to list report of all sku mode vs country for price monitor
    """

    def custom_queryset(self, queryset):
        return SKUCountryQuerysetHandler(queryset).mode()


class AnswerPerCountryReportView(generics.ListAPIView):
    """
    Use this end-point to list report of answer per city for price monitor
    """
    pagination_class = None
    serializer_class = price_monitor_serializers.AnswerReportSerializer
    filterset_class = AnswerPerCountryFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerCountryReportUseCase().execute()


class AnswerPerCityReportView(generics.ListAPIView):
    """
    Use this end-point to list report of answer per country for price monitor
    """
    pagination_class = None
    serializer_class = price_monitor_serializers.AnswerReportSerializer
    filterset_class = AnswerPerCityFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerCityReportUseCase().execute()


class AnswerPerSKUReportView(generics.ListAPIView):
    """
    Use this end-point to list report of answer per sku for price monitor
    """
    pagination_class = None
    serializer_class = price_monitor_serializers.AnswerReportSerializer
    filterset_class = AnswerPerSKUFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerSKUReportUseCase().execute()
