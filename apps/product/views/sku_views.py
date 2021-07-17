from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter

from rest_framework.response import Response

from apps.core import generics
from apps.core.serializers import MessageResponseSerializer
from apps.product.filtersets import SKUFilter
from apps.product.mixins import SKUMixin
from apps.product.serializers import sku_serializers
from apps.product.usecases import sku_usecases


class AddSKUView(generics.CreateAPIView):
    """
    Use this end-point to add new sku
    """
    serializer_class = sku_serializers.AddSKUSerializer

    def perform_create(self, serializer):
        return sku_usecases.AddSKUUseCase(
            serializer=serializer
        ).execute()


class ListSKUView(generics.ListAPIView):
    """
    Use this end-point to list all sku
    """
    serializer_class = sku_serializers.ListSKUSerializer
    filterset_class = SKUFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return sku_usecases.ListSKUUseCase().execute()


class UpdateSKUView(generics.UpdateAPIView, SKUMixin):
    """
    Use this end-point to update specific sku
    """
    serializer_class = sku_serializers.UpdateSKUSerializer

    def get_object(self):
        return self.get_sku()

    def perform_update(self, serializer):
        return sku_usecases.UpdateSKUUseCase(
            serializer=serializer,
            sku=self.get_object()
        ).execute()


class DeleteSKUView(generics.DestroyAPIView, SKUMixin):
    """
    Use this end-point to delete specific sku
    """

    def get_object(self):
        return self.get_sku()

    def perform_destroy(self, instance):
        return sku_usecases.DeleteSKUUseCase(
            sku=self.get_object()
        ).execute()


class ImportSKUView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import sku from the csv file
    """
    serializer_class = sku_serializers.ImportSKUSerializer
    message = _('Imported and saved successfully.')

    def perform_create(self, serializer):
        return sku_usecases.ImportSKUUseCase(
            serializer=serializer
        ).execute()
