from rest_framework import generics

from apps.product.mixins import BrandMixin
from apps.product.serializers import brand_serializers
from apps.product.usecases import brand_usecases
from apps.core.generics import CreateAPIView, ListAPIView


class AddBrandView(CreateAPIView):
    """
    Use this end-point to add new product
    """
    serializer_class = brand_serializers.AddBrandSerializer

    def perform_create(self, serializer):
        return brand_usecases.AddBrandUseCase(
            serializer=serializer
        ).execute()


class ListBrandView(ListAPIView):
    """
    Use this end-point to list all product
    """
    serializer_class = brand_serializers.ListBrandSerializer

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
