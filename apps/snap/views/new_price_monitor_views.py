from apps.snap.serializers import new_price_monitor_serializers
from apps.snap.usecases import new_price_monitor_usecases

# city
from apps.snap.views.base_views import SnapPriceMonitorBaseReportView


class CityMaxPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get max report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CityMinPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get min report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CityMeanPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get mean report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CityModePriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get mode report by city
    """
    serializer_class = new_price_monitor_serializers.CityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.CityModePriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


# Channel
class ChannelMaxPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get max report by Channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class ChannelMinPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get min report by Channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class ChannelMeanPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get mean report by Channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class ChannelModePriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get mode report by channel
    """
    serializer_class = new_price_monitor_serializers.ChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.ChannelModePriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


# Brand
class BrandMaxPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get max report by Brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BrandMinPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get min report by Brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BrandMeanPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get mean report by Brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BrandModePriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to get mode report by brand
    """
    serializer_class = new_price_monitor_serializers.BrandPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_price_monitor_usecases.BrandModePriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()
