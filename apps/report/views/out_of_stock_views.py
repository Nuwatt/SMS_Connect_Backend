from apps.report.filtersets import SKUReportFilter, TotalVisitFilter

from apps.report.serializers import out_of_stock_serializers
from apps.report.serializers.price_monitor_serializers import SKUMonthReportSerializer, TotalVisitReportSerializer
from apps.report.usecases import out_of_stock_usecases
from apps.report.views.base_views import BaseReportView


class OutOfStockReportView(BaseReportView):
    """
    Common class
    """
    filterset_class = SKUReportFilter


class SKUOverallReportView(OutOfStockReportView):
    """
    Use this end-point to list overall report of all sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUOverallReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUOverallReportUseCase().execute()


class SKUMonthAvailableReportView(OutOfStockReportView):
    """
    Use this end-point to list report of month vs available sku for out of stock
    """
    serializer_class = SKUMonthReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUMonthAvailableReportUseCase().execute()


class SKUMonthNotAvailableReportView(OutOfStockReportView):
    """
    Use this end-point to list report of month vs not available sku for out of stock
    """
    serializer_class = SKUMonthReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUMonthNotAvailableReportUseCase().execute()


class SKUMonthLessReportView(OutOfStockReportView):
    """
    Use this end-point to list report of month vs less than 6 sku for out of stock
    """
    serializer_class = SKUMonthReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUMonthLessReportUseCase().execute()


class SKUCityAvailableReportView(OutOfStockReportView):
    """
    Use this end-point to list report of city vs available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUCityReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUCityAvailableReportUseCase().execute()


class SKUCityNotAvailableReportView(OutOfStockReportView):
    """
    Use this end-point to list report of city vs not available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUCityReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUCityNotAvailableReportUseCase().execute()


class SKUCityLessReportView(OutOfStockReportView):
    """
    Use this end-point to list report of city vs less than 6 sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUCityReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUCityLessReportUseCase().execute()


class SKUStoreNotAvailableReportView(OutOfStockReportView):
    """
    Use this end-point to list report of store vs available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUStoreReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUStoreNotAvailableReportUseCase().execute()


class SKURetailerLessReportView(OutOfStockReportView):
    """
    Use this end-point to list report of store vs not available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKURetailerReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKURetailerLessReportUseCase().execute()


class TotalVisitReportView(OutOfStockReportView):
    """
    Use this end-point to list report of total visit for out of stock
    """
    serializer_class = TotalVisitReportSerializer
    filterset_class = TotalVisitFilter

    def get_queryset(self):
        return out_of_stock_usecases.TotalVisitReportUseCase().execute()


class SKUWeekNotAvailableReportView(OutOfStockReportView):
    """
    Use this end-point to list report of last week vs not available sku for out of stock
    """
    serializer_class = out_of_stock_serializers.SKUWeekNotAvailableReportSerializer

    def get_queryset(self):
        return out_of_stock_usecases.SKUWeekNotAvailableReportUseCase().execute()
