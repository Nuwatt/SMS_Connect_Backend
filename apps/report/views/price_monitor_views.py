from apps.core import generics
from apps.report.serializers import price_monitor_serializers
from apps.report.usecases import price_monitor_usecases


class SKUMinMaxReportView(generics.ListAPIView):
    """
    Use this end-point to list report of all sku min max for price monitor
    """
    serializer_class = price_monitor_serializers.SKUMinMaxReportSerializer

    def get_queryset(self):
        return price_monitor_usecases.SKUMinMaxReportUseCase().execute()
