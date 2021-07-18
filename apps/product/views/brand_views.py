from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.core import generics
from apps.product.filtersets import BrandFilter
from apps.product.mixins import BrandMixin
from apps.product.serializers import brand_serializers
from apps.product.usecases import brand_usecases


class AddBrandView(generics.CreateAPIView):
    """
    Use this end-point to add new product
    """
    serializer_class = brand_serializers.AddBrandSerializer

    def perform_create(self, serializer):
        return brand_usecases.AddBrandUseCase(
            serializer=serializer
        ).execute()


class ListBrandView(generics.ListAPIView):
    """
    Use this end-point to list all product
    """
    serializer_class = brand_serializers.ListBrandSerializer
    filterset_class = BrandFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return brand_usecases.ListBrandUseCase().execute()


class UpdateBrandView(generics.UpdateAPIView, BrandMixin):
    """
    Use this end-point to update specific product
    """
    serializer_class = brand_serializers.UpdateBrandSerializer

    def get_object(self):
        return self.get_brand()

    def perform_update(self, serializer):
        return brand_usecases.UpdateBrandUseCase(
            serializer=serializer,
            brand=self.get_object()
        ).execute()


class DeleteBrandView(generics.DestroyAPIView, BrandMixin):
    """
    Use this end-point to delete specific product
    """

    def get_object(self):
        return self.get_brand()

    def perform_destroy(self, instance):
        return brand_usecases.DeleteBrandUseCase(
            brand=self.get_object()
        ).execute()
