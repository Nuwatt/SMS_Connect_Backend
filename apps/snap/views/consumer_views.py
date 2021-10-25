from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, JSONParser

from apps.core import generics
from apps.report.views.base_views import BaseReportView
from apps.snap.filtersets import ConsumerSnapFilter
from apps.snap.mixins import ConsumerSnapMixin
from apps.snap.serializers import consumer_serializers
from apps.snap.usecases import consumer_usecases
from apps.user.permissions import IsPortalUser


class ImportConsumerSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import snap data for consumer
    """
    serializer_class = consumer_serializers.ImportConsumerSnapSerializer
    message = _('Consumer snap imported successfully.')
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return consumer_usecases.ImportConsumerSnapUseCase(
            serializer=serializer
        ).execute()


class ListConsumerSnapView(generics.ListAPIView):
    """
    Use this end-point to list all consumer snap data
    """
    serializer_class = consumer_serializers.ListConsumerSnapSerializer
    permission_classes = (IsPortalUser,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ConsumerSnapFilter
    search_fields = [
        'city__country__name', 'city__name', 'channel__name',
        'sku__category__name', 'sku__brand__name', 'sku__name'
    ]

    def get_queryset(self):
        return consumer_usecases.ListConsumerSnapUseCase().execute()


class UpdateConsumerSnapView(generics.UpdateAPIView, ConsumerSnapMixin):
    """
    Use this end-point to update specific consumer snap data
    """
    serializer_class = consumer_serializers.UpdateConsumerSnapSerializer

    def get_object(self):
        return self.get_consumer_snap()

    def perform_update(self, serializer):
        return consumer_usecases.UpdatePriceMonitorSnapUseCase(
            serializer=serializer,
            consumer_snap=self.get_object()
        ).execute()


class DeleteConsumerSnapView(generics.DestroyAPIView, ConsumerSnapMixin):
    """
    Use this end-point to delete specific consumer snap data
    """
    permission_classes = (IsPortalUser,)

    def get_object(self):
        return self.get_consumer_snap()

    def perform_destroy(self, instance):
        return consumer_usecases.DeleteConsumerSnapUseCase(
            consumer_snap=self.get_object()
        ).execute()


class YesNoQuestionConsumerSnapReportView(BaseReportView):
    """
    Use this end-point to list yes no question report of Consumer Snap
    """
    filterset_class = ConsumerSnapFilter
    serializer_class = consumer_serializers.YesNoQuestionConsumerSnapReportSerializer

    def get_queryset(self):
        return consumer_usecases.YesNoQuestionConsumerSnapUseCase().execute()


class RatingOneToThreeConsumerSnapReportView(BaseReportView):
    """
    Use this end-point to list rating one to three report of Consumer Snap
    """
    filterset_class = ConsumerSnapFilter
    serializer_class = consumer_serializers.RatingOneToThreeConsumerSnapReportSerializer

    def get_queryset(self):
        return consumer_usecases.RatingOneToThreeConsumerSnapUseCase().execute()


class RatingOneToFiveConsumerSnapReportView(BaseReportView):
    """
    Use this end-point to list rating one to five report of Consumer Snap
    """
    filterset_class = ConsumerSnapFilter
    serializer_class = consumer_serializers.RatingOneToFiveConsumerSnapReportSerializer

    def get_queryset(self):
        return consumer_usecases.RatingOneToFiveConsumerSnapUseCase().execute()


class RatingOneToTenConsumerSnapReportView(BaseReportView):
    """
    Use this end-point to list rating one to ten report of Consumer Snap
    """
    filterset_class = ConsumerSnapFilter
    serializer_class = consumer_serializers.RatingOneToTenConsumerSnapReportSerializer

    def get_queryset(self):
        return consumer_usecases.RatingOneToTenConsumerSnapUseCase().execute()


class NumericAverageConsumerSnapReportView(BaseReportView):
    """
    Use this end-point to list numeric average report of Consumer Snap
    """
    filterset_class = ConsumerSnapFilter
    serializer_class = consumer_serializers.NumericAverageConsumerSnapReportSerializer

    def get_queryset(self):
        return consumer_usecases.NumericAverageConsumerSnapUseCase().execute()


class BulkDeleteOutOfStockSnapView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to delete consumer snap in bulk
    """
    serializer_class = consumer_serializers.BulkDeleteConsumerSnapSerializer

    def perform_create(self, serializer):
        return consumer_usecases.BulkDeleteConsumerSnapUseCase(
            serializer=serializer
        ).execute()


class ExportConsumerSnapView(generics.GenericAPIView):
    """
    Use this end-point to export consumer snap to csv file
    """

    def get(self, *args, **kwargs):
        return consumer_usecases.ExportConsumerSnapUseCase().execute()
