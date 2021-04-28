from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.localize.mixins import RegionMixin
from apps.localize.serializers import region_serializers
from apps.localize.usecases import region_usecases


class AddRegionView(CreateAPIView):
    """
    Use this end-point to add new region
    """
    serializer_class = region_serializers.AddRegionSerializer

    def perform_create(self, serializer):
        return region_usecases.AddRegionUseCase(
            serializer=serializer
        ).execute()


class ListRegionView(ListAPIView):
    """
    Use this end-point to list all region
    """
    serializer_class = region_serializers.ListRegionSerializer

    def get_queryset(self):
        return region_usecases.ListRegionUseCase().execute()


class UpdateRegionView(generics.UpdateAPIView, RegionMixin):
    """
    Use this end-point to update specific region
    """
    serializer_class = region_serializers.UpdateRegionSerializer

    def get_object(self):
        return self.get_region()

    def perform_update(self, serializer):
        return region_usecases.UpdateRegionUseCase(
            serializer=serializer,
            region=self.get_object()
        ).execute()


class DeleteRegionView(generics.DestroyAPIView, RegionMixin):
    """
    Use this end-point to delete specific region
    """

    def get_object(self):
        return self.get_region()

    def perform_destroy(self, instance):
        return region_usecases.DeleteRegionUseCase(
            region=self.get_object()
        ).execute()
