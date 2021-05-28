from apps.core import generics
from apps.report.filtersets import SKUMinMaxFilter
from apps.report.queryset_handlers import sku_min_max_queryset_handler
from apps.report.serializers import price_monitor_serializers
from apps.report.usecases import price_monitor_usecases


class SKUMinMaxReportView(generics.ListAPIView):
    """
    Use this end-point to list report of all sku min max for price monitor
    """
    serializer_class = price_monitor_serializers.SKUMinMaxReportSerializer
    filterset_class = SKUMinMaxFilter

    def get_queryset(self):
        return price_monitor_usecases.SKUMinMaxReportUseCase().execute()

    def custom_queryset(self, queryset):
        return sku_min_max_queryset_handler(queryset)
