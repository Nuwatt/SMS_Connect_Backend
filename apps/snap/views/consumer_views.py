from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap import filtersets
from apps.snap.filtersets import SnapConsumerFilter
from apps.snap.mixins import SnapConsumerMixin
from apps.snap.serializers import consumer_serializers
from apps.snap.usecases import consumer_usecases
from apps.user.permissions import IsPortalUser


class ImportSnapConsumerView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import snap data for consumer
    """
    serializer_class = consumer_serializers.ImportSnapConsumerSerializer
    message = _('Consumer snap imported successfully.')
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return consumer_usecases.ImportSnapConsumerUseCase(
            serializer=serializer
        ).execute()


class ListSnapConsumerView(generics.ListAPIView):
    """
    Use this end-point to list all consumer snap data
    """
    serializer_class = consumer_serializers.ListSnapConsumerSerializer
    permission_classes = (IsPortalUser,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SnapConsumerFilter
    search_fields = [
        'city__country__name', 'city__name', 'channel__name',
        'sku__category__name', 'sku__brand__name', 'sku__name'
    ]

    def get_queryset(self):
        return consumer_usecases.ListSnapConsumerUseCase().execute()


class UpdateSnapConsumerView(generics.UpdateAPIView, SnapConsumerMixin):
    """
    Use this end-point to update specific consumer snap data
    """
    serializer_class = consumer_serializers.UpdateSnapConsumerSerializer

    def get_object(self):
        return self.get_consumer_snap()

    def perform_update(self, serializer):
        return consumer_usecases.UpdateSnapConsumerUseCase(
            serializer=serializer,
            consumer_snap=self.get_object()
        ).execute()


class DeleteSnapConsumerView(generics.DestroyAPIView, SnapConsumerMixin):
    """
    Use this end-point to delete specific consumer snap data
    """
    permission_classes = (IsPortalUser,)

    def get_object(self):
        return self.get_consumer_snap()

    def perform_destroy(self, instance):
        return consumer_usecases.DeleteSnapConsumerUseCase(
            consumer_snap=self.get_object()
        ).execute()


class YesNoQuestionSnapConsumerReportView(BaseReportView):
    """
    Use this end-point to list yes no question report of Consumer Snap
    """
    filterset_class = SnapConsumerFilter
    serializer_class = consumer_serializers.YesNoQuestionSnapConsumerReportSerializer

    def get_queryset(self):
        return consumer_usecases.YesNoQuestionSnapConsumerUseCase().execute()


class RatingOneToThreeSnapConsumerReportView(BaseReportView):
    """
    Use this end-point to list rating one to three report of Consumer Snap
    """
    filterset_class = SnapConsumerFilter
    serializer_class = consumer_serializers.RatingOneToThreeSnapConsumerReportSerializer

    def get_queryset(self):
        return consumer_usecases.RatingOneToThreeSnapConsumerUseCase().execute()


class RatingOneToFiveSnapConsumerReportView(BaseReportView):
    """
    Use this end-point to list rating one to five report of Consumer Snap
    """
    filterset_class = SnapConsumerFilter
    serializer_class = consumer_serializers.RatingOneToFiveSnapConsumerReportSerializer

    def get_queryset(self):
        return consumer_usecases.RatingOneToFiveSnapConsumerUseCase().execute()


class RatingOneToTenSnapConsumerReportView(BaseReportView):
    """
    Use this end-point to list rating one to ten report of Consumer Snap
    """
    filterset_class = SnapConsumerFilter
    serializer_class = consumer_serializers.RatingOneToTenSnapConsumerReportSerializer

    def get_queryset(self):
        return consumer_usecases.RatingOneToTenSnapConsumerUseCase().execute()


class NumericAverageSnapConsumerReportView(BaseReportView):
    """
    Use this end-point to list numeric average report of Consumer Snap
    """
    filterset_class = SnapConsumerFilter
    serializer_class = consumer_serializers.NumericAverageSnapConsumerReportSerializer

    def get_queryset(self):
        return consumer_usecases.NumericAverageSnapConsumerUseCase().execute()


class BulkDeleteOutOfStockSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to delete consumer snap in bulk
    """
    serializer_class = consumer_serializers.BulkDeleteSnapConsumerSerializer

    def perform_create(self, serializer):
        return consumer_usecases.BulkDeleteSnapConsumerUseCase(
            serializer=serializer
        ).execute()


class ExportSnapConsumerView(generics.GenericAPIView):
    """
    Use this end-point to export consumer snap to csv file
    """
    filterset_class = filtersets.SnapConsumerFilter

    def get(self, *args, **kwargs):
        return consumer_usecases.ExportConsumerSnapUseCase(
            filter_backends=self.filter_backends,
            request=self.request,
            view_self=self
        ).execute()
