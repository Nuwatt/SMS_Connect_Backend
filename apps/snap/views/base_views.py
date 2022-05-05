from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.snap import filtersets


class SnapBaseReportView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    pagination_class = None
    # permission_classes = [IsAdminPortalUser | IsResearcherPortalUser]


class SnapPriceMonitorBaseReportView(SnapBaseReportView):
    filterset_class = filtersets.SnapPriceMonitorFilter


class SnapOutOfStockBaseReportView(SnapBaseReportView):
    filterset_class = filtersets.SnapOutOfStockFilter


class SnapDistributionBaseReportView(SnapBaseReportView):
    filterset_class = filtersets.SnapDistributionFilter
