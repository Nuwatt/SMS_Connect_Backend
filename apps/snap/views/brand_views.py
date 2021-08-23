from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.core import generics
from apps.snap.filtersets import SnapBrandFilter
from apps.snap.mixins import SnapBrandMixin
from apps.snap.usecases import brand_usecases
from apps.snap.serializers import brand_serializers


class AddSnapBrandView(generics.CreateAPIView):
    """
    Use this end-point to add new snap brand
    """
    serializer_class = brand_serializers.AddSnapBrandSerializer

    def perform_create(self, serializer):
        return brand_usecases.AddSnapBrandUseCase(
            serializer=serializer
        ).execute()


class ListSnapBrandView(generics.ListAPIView):
    """
    Use this end-point to list all snap brand
    """
    serializer_class = brand_serializers.ListSnapBrandSerializer
    filterset_class = SnapBrandFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return brand_usecases.ListSnapBrandUseCase().execute()


class UpdateSnapBrandView(generics.UpdateAPIView, SnapBrandMixin):
    """
    Use this end-point to update specific snap brand
    """
    serializer_class = brand_serializers.UpdateSnapBrandSerializer

    def get_object(self):
        return self.get_snap_brand()

    def perform_update(self, serializer):
        return brand_usecases.UpdateSnapBrandUseCase(
            serializer=serializer,
            snap_brand=self.get_object()
        ).execute()


class DeleteSnapBrandView(generics.DestroyAPIView, SnapBrandMixin):
    """
    Use this end-point to delete specific snap brand
    """

    def get_object(self):
        return self.get_snap_brand()

    def perform_destroy(self, instance):
        return brand_usecases.DeleterSnapBrandUseCase(
            snap_brand=self.get_object()
        ).execute()
