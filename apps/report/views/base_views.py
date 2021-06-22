from apps.core import generics
from apps.core.pagination import ReportPagination
from apps.report.serializers import base_serializers
from apps.report.usecases import base_usecases


class OverviewReportView(generics.RetrieveAPIView):
    """
    Use this end-point to get overview of report
    """
    serializer_class = base_serializers.OverviewReportSerializer

    def get_object(self):
        return base_usecases.OverviewReportUseCase().execute()


class BaseReportView(generics.ListAPIView):
    pagination_class = ReportPagination
