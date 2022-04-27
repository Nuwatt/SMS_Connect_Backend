from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.snap import filtersets
from apps.snap.serializers import new_distribution_serializers
from apps.snap.usecases import new_distribution_usecases


class DistributionSnapReportView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    filterset_class = filtersets.SnapDistributionFilter
    pagination_class = None
    # permission_classes = [IsAdminPortalUser | IsResearcherPortalUser]


class DistributionSnapCityReportView(DistributionSnapReportView):
    """
    Use this end-point to get max report by city
    """
    serializer_class = new_distribution_serializers.DistributionSnapCityReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapCityReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapBrandReportView(DistributionSnapReportView):
    """
    Use this end-point to get max report by Brand
    """
    serializer_class = new_distribution_serializers.DistributionSnapBrandReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapBrandReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapChannelReportView(DistributionSnapReportView):
    """
    Use this end-point to get max report by Channel
    """
    serializer_class = new_distribution_serializers.DistributionSnapChannelReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapChannelReportUseCase(
            sku_provided=sku_provided
        ).execute()


class DistributionSnapSKUReportView(DistributionSnapReportView):
    """
    Use this end-point to get max report by SKU
    """
    serializer_class = new_distribution_serializers.DistributionSnapSKUReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False

        return new_distribution_usecases.DistributionSnapSKUReportUseCase(
            sku_provided=sku_provided
        ).execute()
