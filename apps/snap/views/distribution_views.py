from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap import filtersets
from apps.snap.filtersets import SnapDistributionFilter
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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SnapDistributionFilter
    search_fields = [
        'country_name', 'city_name', 'channel_name',
        'category_name', 'brand_name', 'sku_name'
    ]

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


# class VisitByCountryDistributionSnapReportView(BaseReportView):
#     """
#     Use this end-point to list visit by country report of distribution snap
#     """
#     serializer_class = distribution_serializers.VisitByCountryDistributionSnapReport
#     filterset_class = DistributionSnapFilter
#
#     def get_queryset(self):
#         return distribution_usecases.VisitByCountryDistributionSnapReportUseCase().execute()
#
#
# class VisitByCityDistributionSnapReportView(BaseReportView):
#     """
#     Use this end-point to list visit by city report of distribution snap
#     """
#     serializer_class = distribution_serializers.VisitByCityDistributionSnapReportSerializer
#     filterset_class = DistributionSnapFilter
#
#     def get_queryset(self):
#         return distribution_usecases.VisitByCityDistributionSnapReportUseCase().execute()
#
#
# class VisitByChannelDistributionSnapReportView(BaseReportView):
#     """
#     Use this end-point to list visit by channel report of distribution snap
#     """
#     serializer_class = distribution_serializers.VisitByChannelDistributionSnapReportSerializer
#     filterset_class = DistributionSnapFilter
#
#     def get_queryset(self):
#         return distribution_usecases.VisitByChannelDistributionSnapReportUseCase().execute()
#
#
# class SKUByCityDistributionSnapReportView(BaseReportView):
#     """
#     Use this end-point to list sku by city report of distribution snap
#     """
#     serializer_class = distribution_serializers.SKUByCityDistributionSnapReportSerializer
#     filterset_class = DistributionSnapFilter
#
#     def get_queryset(self):
#         return distribution_usecases.SKUByCityDistributionSnapReportUseCase().execute()


class TotalDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list total distribution of distribution snap
    """
    serializer_class = distribution_serializers.TotalDistributionSnapReportSerializer
    filterset_class = SnapDistributionFilter

    def get_queryset(self):
        return distribution_usecases.TotalDistributionSnapReportUseCase().execute()


class ShelfShareDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list shelf share distribution of distribution snap
    """
    serializer_class = distribution_serializers.ShelfShareDistributionSnapReportSerializer
    filterset_class = SnapDistributionFilter

    def get_queryset(self):
        return distribution_usecases.ShelfShareDistributionSnapReportUseCase().execute()


class NumberOfOutletDistributionSnapReportView(BaseReportView):
    """
    Use this end-point to list number of outlet distribution of distribution snap
    """
    serializer_class = distribution_serializers.NumberOfOutletDistributionSnapReportSerializer
    filterset_class = SnapDistributionFilter

    def get_queryset(self):
        return distribution_usecases.NumberOfOutletDistributionSnapReportUseCase().execute()


class BulkDeleteDistributionSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to delete distribution snap in bulk
    """
    serializer_class = distribution_serializers.BulkDeleteDistributionSnapSerializer

    def perform_create(self, serializer):
        return distribution_usecases.BulkDeleteDistributionSnapUseCase(
            serializer=serializer
        ).execute()


class ExportDistributionSnapView(generics.GenericAPIView):
    """
    Use this end-point to export distribution snap to csv file
    """
    filterset_class = filtersets.SnapDistributionFilter

    def get(self, *args, **kwargs):
        return distribution_usecases.ExportDistributionSnapUseCase(
            filter_backends=self.filter_backends,
            request=self.request,
            view_self=self
        ).execute()
