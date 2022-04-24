from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap.filtersets import SnapOutOfStockFilter
from apps.snap.mixins import PriceMonitorSnapMixin
from apps.snap.serializers import out_of_stock_serializers
from apps.snap.usecases import out_of_stock_usecases
from apps.user.permissions import IsPortalUser


class ImportOutOfStockSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import snap data for out of stock
    """
    serializer_class = out_of_stock_serializers.ImportOutOfStockSnapSerializer
    message = _('Out of Stock snap imported successfully.')
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return out_of_stock_usecases.ImportOutOfStockSnapUseCase(
            serializer=serializer
        ).execute()


class ListOutOfStockSnapView(generics.ListAPIView):
    """
    Use this end-point to list all out of stock snap data
    """
    serializer_class = out_of_stock_serializers.ListOutOfStockSnapSerializer
    permission_classes = (IsPortalUser,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SnapOutOfStockFilter
    search_fields = [
        'country_name', 'city_name', 'channel_name',
        'retailer_name', 'store_name',
        'category_name', 'brand_name', 'sku__name'
    ]

    def get_queryset(self):
        return out_of_stock_usecases.ListOutOfStockSnapUseCase().execute()


class UpdateOutOfStockSnapView(generics.UpdateAPIView, PriceMonitorSnapMixin):
    """
    Use this end-point to update specific out of stock snap data
    """
    serializer_class = out_of_stock_serializers.UpdateOutOfStockSnapSerializer

    def get_object(self):
        return self.get_price_monitor_snap()

    def perform_update(self, serializer):
        return out_of_stock_usecases.UpdatePriceMonitorSnapUseCase(
            serializer=serializer,
            out_of_stock_snap=self.get_object()
        ).execute()


class DeleteOutOfStockSnapView(generics.DestroyAPIView, PriceMonitorSnapMixin):
    """
    Use this end-point to delete specific out of stock snap data
    """
    permission_classes = (IsPortalUser,)

    def get_object(self):
        return self.get_price_monitor_snap()

    def perform_destroy(self, instance):
        return out_of_stock_usecases.DeleteOutOfStockSnapUseCase(
            out_of_stock_snap=self.get_object()
        ).execute()


class OverviewPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list overview report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OverviewOutOfStockSnapReport
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.OverviewOutOfStockSnapReportUseCase().execute()


class AvailableOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list available report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.AvailableOutOfStockSnapReportUseCase().execute()


class NotAvailableOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list not available report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.NotAvailableOutOfStockSnapReportUseCase().execute()


class LessOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list list report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.LessOutOfStockSnapReportUseCase().execute()


# city
class AvailableByCityOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list available by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.ByCityOutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.AvailableByCityOutOfStockSnapReportUseCase().execute()


class NotAvailableByCityOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list not available by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.ByCityOutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.NotAvailableByCityOutOfStockSnapReportUseCase().execute()


class LessByCityOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list less by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.ByCityOutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.LessByCityOutOfStockSnapReportUseCase().execute()


class VisitByCityOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list visit by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.VisitByCityOutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.VisitByCityOutOfStockSnapReportUseCase().execute()


class NotAvailableByWeekOutOfStockSnapReportView(BaseReportView):
    """
    Use this end-point to list not available by week report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.NotAvailableByWeekOutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        return out_of_stock_usecases.NotAvailableByWeekOutOfStockSnapReportUseCase().execute()


class BulkDeleteOutOfStockSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to delete out of stock snap in bulk
    """
    serializer_class = out_of_stock_serializers.BulkDeleteOutOfStockSnapSerializer

    def perform_create(self, serializer):
        return out_of_stock_usecases.BulkDeleteOutOfStockSnapUseCase(
            serializer=serializer
        ).execute()


class ExportOutOfStockSnapView(generics.GenericAPIView):
    """
    Use this end-point to export out of stock to csv file
    """

    def get(self, *args, **kwargs):
        return out_of_stock_usecases.ExportOutOfStockSnapUseCase().execute()
