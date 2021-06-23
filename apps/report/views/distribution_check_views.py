from apps.core import generics
from apps.report.filtersets.base_filtersets import ResponseFilter, SKUResponseFilter
from apps.report.serializers import distribution_check_serializers
from apps.report.usecases import distribution_check_usecases


from apps.report.views.base_views import BaseReportView


class VisitPerCountryReportView(BaseReportView):
    """
    Use this end-point to list report of visit per country for distribution check
    """
    serializer_class = distribution_check_serializers.VisitPerCountryReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.VisitPerCountryReportUseCase().execute()


# optimized
class VisitPerCityReportView(generics.ListAPIView):
    """
    Use this end-point to list report of visit per city for distribution check
    """
    serializer_class = distribution_check_serializers.VisitPerCityReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.VisitPerCityReportUseCase().execute()


# optimized
class VisitPerChannelReportView(generics.ListAPIView):
    """
    Use this end-point to list report of visit per channel for distribution check
    """
    serializer_class = distribution_check_serializers.VisitPerChannelReportSerializer
    filterset_class = ResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.VisitPerChannelReportUseCase().execute()


class SKUPerCityReportView(generics.ListAPIView):
    """
    Use this end-point to list report of total sku per city for distribution check
    """
    serializer_class = distribution_check_serializers.SKUPerCityReportSerializer
    filterset_class = SKUResponseFilter

    def get_queryset(self):
        return distribution_check_usecases.SKUPerCityReportUseCase().execute()