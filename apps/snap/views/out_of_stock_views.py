from django.utils.translation import gettext_lazy as _
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap.filtersets import OutOfStockSnapFilter
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

#
# class OverviewPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list overview report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.OverviewPriceMonitorSnapReport
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.OverviewPriceMonitorSnapReportUseCase().execute()
#
#
# class MonthMaxPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list month max report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.MonthPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.MonthMaxPriceMonitorSnapReportUseCase().execute()
#
#
# class MonthMinPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list month min report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.MonthPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.MonthMinPriceMonitorSnapReportUseCase().execute()
#
#
# class MonthModePriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list month mode report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.MonthPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.MonthModePriceMonitorSnapReportUseCase().execute()
#
#
# class MonthMeanPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list month mean report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.MonthPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.MonthMeanPriceMonitorSnapReportUseCase().execute()
#
#
# class BrandOverviewPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list brand overview report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.BrandoverviewPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.BrandOverviewPriceMonitorSnapReportUseCase().execute()
#
#
# class CountryMinPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list country min report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.CountryPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.CountryMinPriceMonitorSnapReportUseCase().execute()
#
#
# class CountryMaxPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list country max report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.CountryPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.CountryMaxPriceMonitorSnapReportUseCase().execute()
#
#
# class CountryMeanPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list country mean report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.CountryPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.CountryMeanPriceMonitorSnapReportUseCase().execute()
#
#
# class CountryModePriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list country mode report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.CountryPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.CountryModePriceMonitorSnapReportUseCase().execute()
#
#
# class VisitPerCityPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list visit per city report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.VisitPerCityPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.VisitPerCityPriceMonitorSnapReportUseCase().execute()
#
#
# class VisitPerCountryPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list visit per country report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.VisitPerCountryPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.VisitPerCountryPriceMonitorSnapReportUseCase().execute()
#
#
# class SKUPerChannelPriceMonitorSnapReportView(BaseReportView):
#     """
#     Use this end-point to list sku per channel report of out of stock snap
#     """
#     serializer_class = out_of_stock_serializers.SKUPerChannelPriceMonitorSnapReportSerializer
#     filterset_class = OutOfStockSnapFilter
#
#     def get_queryset(self):
#         return out_of_stock_usecases.SKUPerChannelPriceMonitorSnapReportUseCase().execute()
