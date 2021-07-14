from apps.report.filtersets import out_of_stock_filtersets
from apps.report.filtersets.base_filtersets import SKUResponseFilter, ResponseFilter

from apps.report.serializers import out_of_stock_serializers
from apps.report.serializers.price_monitor_serializers import (
    SKUMonthReportSerializer,
    TotalVisitReportSerializer
)
from apps.report.usecases import out_of_stock_usecases
from apps.report.views.base_views import BaseReportView


class SKUOverallReportView(BaseReportView):
    """
    Use this end-point to list overall report of all sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUOverallReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUOverallReportUseCase().execute()


class SKUMonthAvailableReportView(BaseReportView):
    """
    Use this end-point to list report of month vs available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUMonthAvailableReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUMonthAvailableReportUseCase().execute()


class SKUMonthNotAvailableReportView(BaseReportView):
    """
    Use this end-point to list report of month vs not available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUMonthNotAvailableReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUMonthNotAvailableReportUseCase().execute()


class SKUMonthLessReportView(BaseReportView):
    """
    Use this end-point to list report of month vs less than 6 sku for out of stock
    """
    serializer_class = SKUMonthReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUMonthLessReportUseCase().execute()


class SKUCityAvailableReportView(BaseReportView):
    """
    Use this end-point to list report of city vs available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUCityReportSerializer
    filterset_class = out_of_stock_filtersets.SKUCityReportFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUCityAvailableReportUseCase().execute()


class SKUCityNotAvailableReportView(BaseReportView):
    """
    Use this end-point to list report of city vs not available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUCityReportSerializer
    filterset_class = out_of_stock_filtersets.SKUCityReportFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUCityNotAvailableReportUseCase().execute()


class SKUCityLessReportView(BaseReportView):
    """
    Use this end-point to list report of city vs less than 6 sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUCityReportSerializer
    filterset_class = out_of_stock_filtersets.SKUCityReportFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUCityLessReportUseCase().execute()


class SKUStoreNotAvailableReportView(BaseReportView):
    """
    Use this end-point to list report of store vs available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUStoreReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUStoreNotAvailableReportUseCase().execute()


class TotalVisitReportView(BaseReportView):
    """
    Use this end-point to list report of total visit for out of stock
    """
    serializer_class = TotalVisitReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.TotalVisitReportUseCase().execute()


class SKUWeekNotAvailableReportView(BaseReportView):
    """
    Use this end-point to list report of last week vs not available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUWeekNotAvailableReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return out_of_stock_usecases.SKUWeekNotAvailableReportUseCase().execute()
