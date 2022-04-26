from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.snap import filtersets
from apps.snap.serializers import new_price_monitor_serializers
from apps.snap.usecases import new_price_monitor_usecases


class SnapBaseReportView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    filterset_class = filtersets.SnapPriceMonitorFilter
    pagination_class = None
    # permission_classes = [IsAdminPortalUser | IsResearcherPortalUser]


class CityMaxPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get report by city
    """
    serializer_class = new_price_monitor_serializers.CityMaxPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()
