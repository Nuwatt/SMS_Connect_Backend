from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.snap.filtersets import SnapOutOfStockFilter
from apps.snap.mixins import PriceMonitorSnapMixin
from apps.snap.serializers import out_of_stock_serializers
from apps.snap.usecases import out_of_stock_usecases
from apps.snap.views.base_views import SnapOutOfStockBaseReportView
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
        return out_of_stock_usecases.UpdateOutOfStockSnapUseCase(
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


class OverviewPriceMonitorSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list overview report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OverviewOutOfStockSnapReport

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.OverviewOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class AvailableOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list available report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OutOfStockSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.AvailableOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class NotAvailableOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list not available report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OutOfStockSnapReportSerializer
    filterset_class = SnapOutOfStockFilter

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.NotAvailableOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class LessOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list list report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.OutOfStockSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.LessOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


# city
class AvailableByCityOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list available by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.ByCityOutOfStockSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.AvailableByCityOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class NotAvailableByCityOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list not available by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.ByCityOutOfStockSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.NotAvailableByCityOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class LessByCityOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list less by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.ByCityOutOfStockSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.LessByCityOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class VisitByCityOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list visit by city report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.VisitByCityOutOfStockSnapReportSerializer

    def get_queryset(self):
        city_provided = True if self.request.GET.get('city', None) else False
        return out_of_stock_usecases.VisitByCityOutOfStockSnapReportUseCase(
            city_provided=city_provided
        ).execute()


class NotAvailableByWeekOutOfStockSnapReportView(SnapOutOfStockBaseReportView):
    """
    Use this end-point to list not available by week report of out of stock snap
    """
    serializer_class = out_of_stock_serializers.NotAvailableByWeekOutOfStockSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return out_of_stock_usecases.NotAvailableByWeekOutOfStockSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


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
