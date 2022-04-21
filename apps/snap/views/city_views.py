from apps.core import generics
from apps.snap.filtersets import SnapCityFilter
from apps.snap.serializers import city_serializers
from apps.snap.usecases import city_usecases
from apps.snap.mixins import SnapCityMixin


class AddSnapCityView(generics.CreateAPIView):
    """
    Use this end-point to add new snap snap_city
    """
    serializer_class = city_serializers.AddSnapCitySerializer

    def perform_create(self, serializer):
        return city_usecases.AddSnapCityUseCase(
            serializer=serializer
        ).execute()


class ListSnapCityView(generics.ListAPIView):
    """
    Use this end-point to list all snap cities
    """
    serializer_class = city_serializers.ListSnapCitySerializer
    filterset_class = SnapCityFilter

    def get_queryset(self):
        return city_usecases.ListSnapCityUseCase().execute()


class UpdateSnapCityView(generics.UpdateAPIView, SnapCityMixin):
    """
    Use this end-point to update specific snap snap_city
    """
    serializer_class = city_serializers.UpdateSnapCitySerializer

    def get_object(self):
        return self.get_snap_city()

    def perform_update(self, serializer):
        return city_usecases.UpdateSnapCityUseCase(
            serializer=serializer,
            snap_city=self.get_object()
        ).execute()


class DeleteSnapCityView(generics.DestroyAPIView, SnapCityMixin):
    """
    Use this end-point to delete specific snap snap_city
    """

    def get_object(self):
        return self.get_snap_city()

    def perform_destroy(self, instance):
        return city_usecases.DeleteSnapCityUseCase(
            snap_city=self.get_object()
        ).execute()
