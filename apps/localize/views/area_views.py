from apps.core import generics
from apps.localize.filtersets import AreaFilter
from apps.localize.mixins import AreaMixin
from apps.localize.serializers import area_serializers
from apps.localize.usecases import area_usecases


class AddAreaView(generics.CreateAPIView):
    """
    Use this end-point to add new area
    """
    serializer_class = area_serializers.AddAreaSerializer

    def perform_create(self, serializer):
        return area_usecases.AddAreaUseCase(
            serializer=serializer
        ).execute()


class ListAreaView(generics.ListAPIView):
    """
    Use this end-point to list all areas
    """
    serializer_class = area_serializers.ListAreaSerializer
    filterset_class = AreaFilter

    def get_queryset(self):
        return area_usecases.ListAreaUseCase().execute()


class UpdateAreaView(generics.UpdateAPIView, AreaMixin):
    """
    Use this end-point to update specific area
    """
    serializer_class = area_serializers.UpdateAreaSerializer

    def get_object(self):
        return self.get_area()

    def perform_update(self, serializer):
        return area_usecases.UpdateAreaUseCase(
            serializer=serializer,
            area=self.get_object()
        ).execute()


class DeleteAreaView(generics.DestroyAPIView, AreaMixin):
    """
    Use this end-point to delete specific area
    """

    def get_object(self):
        return self.get_area()

    def perform_destroy(self, instance):
        return area_usecases.DeleteAreaUseCase(
            area=self.get_object()
        ).execute()
