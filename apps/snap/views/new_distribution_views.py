from apps.snap.serializers import new_distribution_serializers
from apps.snap.usecases import new_distribution_usecases
from apps.snap.views.base_views import SnapDistributionBaseReportView


class DistributionSnapCityReportView(SnapDistributionBaseReportView):
    """
    Use this end-point to get max report by city
    """
    serializer_class = new_distribution_serializers.DistributionSnapCityReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapCityReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapCountryReportView(SnapDistributionBaseReportView):
    """
    Use this end-point to get max report by country
    """
    serializer_class = new_distribution_serializers.DistributionSnapCountryReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapCountryReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapBrandReportView(SnapDistributionBaseReportView):
    """
    Use this end-point to get max report by Brand
    """
    serializer_class = new_distribution_serializers.DistributionSnapBrandReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapBrandReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapChannelReportView(SnapDistributionBaseReportView):
    """
    Use this end-point to get max report by Channel
    """
    serializer_class = new_distribution_serializers.DistributionSnapChannelReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapChannelReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapSKUReportView(SnapDistributionBaseReportView):
    """
    Use this end-point to get max report by SKU
    """
    serializer_class = new_distribution_serializers.DistributionSnapSKUReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapSKUReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapChannelCityReportView(SnapDistributionBaseReportView):
    """
    Use this end-point to get max report by Channel city
    """
    serializer_class = new_distribution_serializers.DistributionSnapChannelCityReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapChannelCityReportUseCase(
            sku_provided=sku_provided
        ).execute()
