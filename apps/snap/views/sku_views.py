from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


from apps.core import generics
from apps.snap.filtersets import SnapSKUFilter
from apps.snap.mixins import SnapSKUMixin
from apps.snap.usecases import sku_usecases
from apps.snap.serializers import sku_serializers


class AddSnapSKUView(generics.CreateAPIView):
    """
    Use this end-point to add new snap sku
    """
    serializer_class = sku_serializers.AddSnapSKUSerializer

    def perform_create(self, serializer):
        return sku_usecases.AddSnapSKUUseCase(
            serializer=serializer
        ).execute()


class ListSnapSKUView(generics.ListAPIView):
    """
    Use this end-point to list all snap sku
    """
    serializer_class = sku_serializers.ListSnapSKUSerializer
    filterset_class = SnapSKUFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return sku_usecases.ListSnapSKUUseCase().execute()


class UpdateSnapSKUView(generics.UpdateAPIView, SnapSKUMixin):
    """
    Use this end-point to update specific snap sku
    """
    serializer_class = sku_serializers.UpdateSnapSKUSerializer

    def get_object(self):
        return self.get_snap_sku()

    def perform_update(self, serializer):
        return sku_usecases.UpdateSnapSKUUseCase(
            serializer=serializer,
            snap_sku=self.get_object()
        ).execute()


class DeleteSnapSKUView(generics.DestroyAPIView, SnapSKUMixin):
    """
    Use this end-point to delete specific snap sku
    """

    def get_object(self):
        return self.get_snap_sku()

    def perform_destroy(self, instance):
        return sku_usecases.DeleteSnapSKUUseCase(
            snap_sku=self.get_object()
        ).execute()
