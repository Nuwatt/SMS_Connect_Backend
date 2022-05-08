from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.snap import filtersets
from apps.snap.mixins import PriceMonitorSnapMixin
from apps.snap.serializers import price_monitor_serializers
from apps.snap.usecases import price_monitor_usecases
from apps.snap.views.base_views import SnapPriceMonitorBaseReportView
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
    filterset_class = filtersets.SnapPriceMonitorFilter
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        return price_monitor_usecases.ExportPriceMonitorSnapUseCase(
            filter_backends=self.filter_backends,
            request=self.request,
            view_self=self
        ).execute()


class ListPriceMonitorSnapView(generics.ListAPIView):
    """
    Use this end-point to list all price monitor snap data
    """
    serializer_class = price_monitor_serializers.ListPriceMonitorSnapSerializer
    permission_classes = (IsPortalUser,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = filtersets.SnapPriceMonitorFilter
    search_fields = [
        'country_name', 'city_name', 'channel_name',
        'category_name', 'brand_name', 'sku_name',
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


class OverviewPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list overview report of price monitor snap
    """
    serializer_class = price_monitor_serializers.OverviewPriceMonitorSnapReport

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.OverviewPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class MonthMaxPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list month max report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.MonthMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class MonthMinPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list month min report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.MonthMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class MonthModePriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list month mode report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.MonthModePriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class MonthMeanPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list month mean report of price monitor snap
    """
    serializer_class = price_monitor_serializers.MonthPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.MonthMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BrandOverviewPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list brand overview report of price monitor snap
    """
    serializer_class = price_monitor_serializers.BrandoverviewPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.BrandOverviewPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()

    # def custom_queryset(self, queryset):
    #     results = []
    #     unique_brands = queryset.values('brand_id', 'brand_name').distinct()
    #     stats = queryset.aggregate(
    #         Min('min'),
    #         Max('max'),
    #         Avg('mean')
    #     )
    #
    #     for brand in unique_brands:
    #         results.append({
    #             'brand_name': brand.get('brand_name'),
    #             'mode_value': queryset.annotate(
    #                 Count('mode')
    #             ).order_by('-mode__count').values('mode')[0].get('mode'),
    #             'min_value': stats.get('min__min'),
    #             'max_value': stats.get('max__max'),
    #             'mean_value': stats.get('mean__avg'),
    #         })
    #
    #     return results


class CountryMinPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list country min report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.CountryMinPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CountryMaxPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list country max report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.CountryMaxPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CountryMeanPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list country mean report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.CountryMeanPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class CountryModePriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list country mode report of price monitor snap
    """
    serializer_class = price_monitor_serializers.CountryPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.CountryModePriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class VisitPerCityPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list visit per city report of price monitor snap
    """
    serializer_class = price_monitor_serializers.VisitPerCityPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.VisitPerCityPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class VisitPerCountryPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list visit per country report of price monitor snap
    """
    serializer_class = price_monitor_serializers.VisitPerCountryPriceMonitorSnapReportSerializer

    def get_queryset(self):
        country_provided = True if self.request.GET.get('country', None) else False
        return price_monitor_usecases.VisitPerCountryPriceMonitorSnapReportUseCase(
            country_provided=country_provided
        ).execute()


class SKUPerChannelPriceMonitorSnapReportView(SnapPriceMonitorBaseReportView):
    """
    Use this end-point to list sku per channel report of price monitor snap
    """
    serializer_class = price_monitor_serializers.SKUPerChannelPriceMonitorSnapReportSerializer

    def get_queryset(self):
        sku_provided = True if self.request.GET.get('sku', None) else False
        return price_monitor_usecases.SKUPerChannelPriceMonitorSnapReportUseCase(
            sku_provided=sku_provided
        ).execute()


class BulkDeletePriceMonitorSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to delete price monitor snap in bulk
    """
    serializer_class = price_monitor_serializers.BulkDeletePriceMonitorSnapSerializer

    def perform_create(self, serializer):
        return price_monitor_usecases.BulkDeletePriceMonitorSnapUseCase(
            serializer=serializer
        ).execute()
