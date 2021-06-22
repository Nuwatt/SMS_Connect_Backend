from apps.core import generics
from apps.core.pagination import ReportPagination
from apps.report import filtersets
from apps.report.serializers import price_monitor_serializers
from apps.report.usecases import price_monitor_usecases


# optimized
class SKUMinMaxReportView(generics.ListAPIView):
    """
    Use this end-point to list report of all sku min max for price monitor
    """
    serializer_class = price_monitor_serializers.SKUMinMaxReportSerializer
    filterset_class = filtersets.ResponseFilter
    pagination_class = ReportPagination

    def get_queryset(self):
        return price_monitor_usecases.SKUMinMaxReportUseCase().execute()


class SKUMonthReportView(generics.ListAPIView):
    """
    Common SKU Month
    """

    serializer_class = price_monitor_serializers.SKUMonthReportSerializer
    filterset_class = filtersets.SKUMonthReportFilter
    pagination_class = ReportPagination


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


class SKUCountryReportView(generics.ListAPIView):
    """
    Common SKU Country Report
    """
    serializer_class = price_monitor_serializers.SKUCountryReportSerializer
    filterset_class = filtersets.SKUCountryReportFilter
    pagination_class = ReportPagination


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
class AnswerPerCountryReportView(generics.ListAPIView):
    """
    Use this end-point to list report of answer per country for price monitor
    """
    pagination_class = ReportPagination
    serializer_class = price_monitor_serializers.AnswerPerCountryReportSerializer
    filterset_class = filtersets.AnswerPerCountryReportFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerCountryReportUseCase().execute()


# optimized
class AnswerPerCityReportView(generics.ListAPIView):
    """
    Use this end-point to list report of answer per country for price monitor
    """
    pagination_class = ReportPagination
    serializer_class = price_monitor_serializers.AnswerPerCityReportSerializer
    filterset_class = filtersets.AnswerPerCityReportFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerCityReportUseCase().execute()


# optimized
class AnswerPerSKUReportView(generics.ListAPIView):
    """
    Use this end-point to list report of answer per sku for price monitor
    """
    pagination_class = ReportPagination
    serializer_class = price_monitor_serializers.AnswerReportSerializer
    filterset_class = filtersets.AnswerPerSKUReportFilter

    def get_queryset(self):
        return price_monitor_usecases.AnswerPerSKUReportUseCase().execute()


# optimized
class TotalVisitReportView(generics.ListAPIView):
    """
    Use this end-point to list report of total visit for price monitor
    """
    pagination_class = ReportPagination
    serializer_class = price_monitor_serializers.TotalVisitReportSerializer
    filterset_class = filtersets.TotalVisitFilter

    def get_queryset(self):
        return price_monitor_usecases.TotalVisitReportUseCase().execute()


class BrandMinMaxReportView(generics.ListAPIView):
    """
    Use this end-point to list report of brand vs min max for price monitor
    """
    pagination_class = ReportPagination
    serializer_class = price_monitor_serializers.BrandMinMaxReportSerializer
    filterset_class = filtersets.BrandMinMaxReportFilter

    def get_queryset(self):
        return price_monitor_usecases.BrandMinMaxReportReportUseCase().execute()
