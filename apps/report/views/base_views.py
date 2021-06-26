from apps.core import generics
from apps.core.pagination import ReportPagination
from apps.report.serializers import base_serializers
from apps.report.usecases import base_usecases
from apps.user.permissions import IsAdminPortalUser, IsResearcherPortalUser


class OverviewReportView(generics.RetrieveAPIView):
    """
    Use this end-point to get overview of report
    """
    serializer_class = base_serializers.OverviewReportSerializer
    permission_classes = [IsAdminPortalUser | IsResearcherPortalUser]

    def get_object(self):
        return base_usecases.OverviewReportUseCase().execute()


class BaseReportView(generics.ListAPIView):
    pagination_class = ReportPagination
    permission_classes = [IsAdminPortalUser | IsResearcherPortalUser]
