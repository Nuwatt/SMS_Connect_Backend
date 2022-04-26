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


# city
class CityMaxPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get max report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CityMinPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get min report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CityMeanPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get mean report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


# Channel
class ChannelMaxPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get max report by Channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class ChannelMinPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get min report by Channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class ChannelMeanPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get mean report by Channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


# Brand
class BrandMaxPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get max report by Brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BrandMinPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get min report by Brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BrandMeanPriceMonitorSnapReportView(SnapBaseReportView):
    """
    Use this end-point to get mean report by Brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()
