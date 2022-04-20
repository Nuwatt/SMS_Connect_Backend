from django.db.models import Count, Min, Max, Avg
from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap import filtersets
from apps.snap.filtersets import PriceMonitorSnapFilter
from apps.snap.mixins import PriceMonitorSnapMixin
from apps.snap.serializers import price_monitor_serializers
from apps.snap.usecases import price_monitor_usecases
from apps.user.permissions import IsPortalUser


class ImportPriceMonitorSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import snap data for price monitor
    """
    serializer_class = price_monitor_serializers.ImportPriceMonitorSnapSerializer
    message = _('Price Monitor snap imported successfully.')
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return price_monitor_usecases.ImportPriceMonitorSnapUseCase(
            serializer=serializer
        ).execute()


class ExportPriceMonitorSnapView(generics.GenericAPIView):
    """
    Use this end-point to export price monitor to csv file
    """

    def get(self, *args, **kwargs):
        return price_monitor_usecases.ExportPriceMonitorSnapUseCase().execute()


class ListPriceMonitorSnapView(generics.ListAPIView):
    """
    Use this end-point to list all price monitor snap data
    """
    serializer_class = price_monitor_serializers.ListPriceMonitorSnapSerializer
    permission_classes = (IsPortalUser,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PriceMonitorSnapFilter
    search_fields = [
        'city__country__name', 'city__name', 'channel__name',
        'sku__category__name', 'sku__brand__name', 'sku__name',
        'count', 'min', 'min', 'max', 'mean', 'mode'
    ]

    def get_queryset(self):
        return price_monitor_usecases.ListPriceMonitorSnapUseCase().execute()


class UpdatePriceMonitorSnapView(generics.UpdateAPIView, PriceMonitorSnapMixin):
    """
    Use this end-point to update specific price monitor snap data
    """
    serializer_class = price_monitor_serializers.UpdatePriceMonitorSnapSerializer

    def get_object(self):
        return self.get_price_monitor_snap()

    def perform_update(self, serializer):
        return price_monitor_usecases.UpdatePriceMonitorSnapUseCase(
            serializer=serializer,
            price_monitor_snap=self.get_object()
        ).execute()


class DeletePriceMonitorSnapView(generics.DestroyAPIView, PriceMonitorSnapMixin):
    """
    Use this end-point to delete specific price monitor snap data
    """
    permission_classes = (IsPortalUser,)

    def get_object(self):
        return self.get_price_monitor_snap()

    def perform_destroy(self, instance):
        return price_monitor_usecases.DeletePriceMonitorSnapUseCase(
            price_monitor_snap=self.get_object()
        ).execute()


class OverviewPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list overview report of price monitor snap
    """
    serializer_class = price_monitor_serializers.OverviewPriceMonitorSnapReport
    filterset_class = filtersets.SnapPriceMonitorFilter

    def get_queryset(self):
        return price_monitor_usecases.OverviewPriceMonitorSnapReportUseCase().execute()


class MonthMaxPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list month max report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.MonthMaxPriceMonitorSnapReportUseCase().execute()


class MonthMinPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list month min report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.MonthMinPriceMonitorSnapReportUseCase().execute()


class MonthModePriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list month mode report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.MonthModePriceMonitorSnapReportUseCase().execute()


class MonthMeanPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list month mean report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.MonthMeanPriceMonitorSnapReportUseCase().execute()


class BrandOverviewPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list brand overview report of price monitor snap
    """
    serializer_class = price_monitor_serializers.BrandoverviewPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.BrandOverviewPriceMonitorSnapReportUseCase().execute()

    def custom_queryset(self, queryset):
        results = []
        unique_brands = queryset.values('sku__brand_id', 'sku__brand__name').distinct()
        stats = queryset.aggregate(
            Min('min'),
            Max('max'),
            Avg('mean')
        )

        for brand in unique_brands:
            results.append({
                'brand_name': brand.get('sku__brand__name'),
                'mode_value': queryset.annotate(
                    Count('mode')
                ).order_by('-mode__count').values('mode')[0].get('mode'),
                'min_value': stats.get('min__min'),
                'max_value': stats.get('max__max'),
                'mean_value': stats.get('mean__avg'),
            })

        return results


class CountryMinPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list country min report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.CountryMinPriceMonitorSnapReportUseCase().execute()


class CountryMaxPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list country max report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.CountryMaxPriceMonitorSnapReportUseCase().execute()


class CountryMeanPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list country mean report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.CountryMeanPriceMonitorSnapReportUseCase().execute()


class CountryModePriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list country mode report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.CountryModePriceMonitorSnapReportUseCase().execute()


class VisitPerCityPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list visit per city report of price monitor snap
    """
    serializer_class = price_monitor_serializers.VisitPerCityPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.VisitPerCityPriceMonitorSnapReportUseCase().execute()


class VisitPerCountryPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list visit per country report of price monitor snap
    """
    serializer_class = price_monitor_serializers.VisitPerCountryPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.VisitPerCountryPriceMonitorSnapReportUseCase().execute()


class SKUPerChannelPriceMonitorSnapReportView(BaseReportView):
    """
    Use this end-point to list sku per channel report of price monitor snap
    """
    serializer_class = price_monitor_serializers.SKUPerChannelPriceMonitorSnapReportSerializer
    filterset_class = PriceMonitorSnapFilter

    def get_queryset(self):
        return price_monitor_usecases.SKUPerChannelPriceMonitorSnapReportUseCase().execute()


class BulkDeletePriceMonitorSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to delete price monitor snap in bulk
    """
    serializer_class = price_monitor_serializers.BulkDeletePriceMonitorSnapSerializer

    def perform_create(self, serializer):
        return price_monitor_usecases.BulkDeletePriceMonitorSnapUseCase(
            serializer=serializer
        ).execute()
