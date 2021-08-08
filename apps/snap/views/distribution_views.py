from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap.filtersets import DistributionSnapFilter
from apps.snap.mixins import DistributionSnapMixin
from apps.snap.serializers import distribution_serializers
from apps.snap.usecases import distribution_usecases
from apps.user.permissions import IsPortalUser


class ImportDistributionSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import snap data for distribution
    """
    serializer_class = distribution_serializers.ImportDistributionSnapSerializer
    message = _('Distribution snap imported successfully.')
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return distribution_usecases.ImportDistributionSnapUseCase(
            serializer=serializer
        ).execute()


class ListDistributionSnapView(generics.ListAPIView):
    """
    Use this end-point to list all distribution snap data
    """
    serializer_class = distribution_serializers.ListDistributionSnapSerializer
    permission_classes = (IsPortalUser,)

    def get_queryset(self):
        return distribution_usecases.ListDistributionSnapUseCase().execute()


class UpdateDistributionSnapView(generics.UpdateAPIView, DistributionSnapMixin):
    """
    Use this end-point to update specific distribution snap data
    """
    serializer_class = distribution_serializers.UpdateDistributionSnapSerializer

    def get_object(self):
        return self.get_distribution_snap()

    def perform_update(self, serializer):
        return distribution_usecases.UpdateDistributionSnapUseCase(
            serializer=serializer,
            price_monitor_snap=self.get_object()
        ).execute()


class DeleteDistributionSnapView(generics.DestroyAPIView, DistributionSnapMixin):
    """
    Use this end-point to delete specific distribution snap data
    """
    permission_classes = (IsPortalUser,)

    def get_object(self):
        return self.get_distribution_snap()

    def perform_destroy(self, instance):
        return distribution_usecases.DeleteDistributionSnapUseCase(
            price_monitor_snap=self.get_object()
        ).execute()


class VisitByCountryDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list visit by country report of distribution snap
    """
    serializer_class = distribution_serializers.VisitByCountryDistributionSnapReport
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.VisitByCountryDistributionSnapReportUseCase().execute()


class VisitByCityDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list visit by city report of distribution snap
    """
    serializer_class = distribution_serializers.VisitByCityDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.VisitByCityDistributionSnapReportUseCase().execute()


class VisitByChannelDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list visit by channel report of distribution snap
    """
    serializer_class = distribution_serializers.VisitByChannelDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.VisitByChannelDistributionSnapReportUseCase().execute()


class SKUByCityDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list sku by city report of distribution snap
    """
    serializer_class = distribution_serializers.SKUByCityDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.SKUByCityDistributionSnapReportUseCase().execute()


class SKUByCountryDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list sku by country report of distribution snap
    """
    serializer_class = distribution_serializers.SKUByCountryDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.SKUByCountryDistributionSnapReportUseCase().execute()


class SKUByChannelDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list sku by channel report of distribution snap
    """
    serializer_class = distribution_serializers.SKUByChannelDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.SKUByChannelDistributionSnapReportUseCase().execute()


class ShareSKUByCountryDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list share sku by country report of distribution snap
    """
    serializer_class = distribution_serializers.ShareSKUByCountryDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.ShareSKUByCountryDistributionSnapReportUseCase().execute()


class ShareSKUByChannelDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list share sku by channel report of distribution snap
    """
    serializer_class = distribution_serializers.ShareSKUByChannelDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.ShareSKUByChannelDistributionSnapReportUseCase().execute()


class ShareBrandByCountryDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list share brand by country report of distribution snap
    """
    serializer_class = distribution_serializers.ShareBrandByCountryDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.ShareBrandByCountryDistributionSnapReportUseCase().execute()


class ShareBrandByChannelDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list share brand by channel report of distribution snap
    """
    serializer_class = distribution_serializers.ShareBrandByChannelDistributionSnapReportSerializer
    filterset_class = DistributionSnapFilter

    def get_queryset(self):
        return distribution_usecases.ShareBrandByChannelDistributionSnapReportUseCase().execute()
