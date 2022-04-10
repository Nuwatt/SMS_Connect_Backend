from apps.core import generics
from apps.snap.filtersets import SnapCountryFilter
from apps.snap.mixins import SnapCountryMixin
from apps.snap.serializers import country_serializers
from apps.snap.usecases import country_usecases


class AddSnapCountryView(generics.CreateAPIView):
    """
    Use this end-point to add new snap country
    """
    serializer_class = country_serializers.AddSnapCountrySerializer

    def perform_create(self, serializer):
        return country_usecases.AddCountryUseCase(
            serializer=serializer
        ).execute()


class ListSnapCountryView(generics.ListAPIView):
    """
    Use this end-point to list all snap country
    """
    serializer_class = country_serializers.ListSnapCountrySerializer
    filterset_class = SnapCountryFilter

    def get_queryset(self):
        return country_usecases.ListCountryUseCase().execute()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateSnapCountryView(generics.UpdateAPIView, SnapCountryMixin):
    """
    Use this end-point to update specific snap country
    """
    serializer_class = country_serializers.UpdateSnapCountrySerializer

    def get_object(self):
        return self.get_snap_country()

    def perform_update(self, serializer):
        return country_usecases.UpdateCountryUseCase(
            serializer=serializer,
            country=self.get_object()
        ).execute()


class DeleteSnapCountryView(generics.DestroyAPIView, SnapCountryMixin):
    """
    Use this end-point to delete specific snap country
    """

    def get_object(self):
        return self.get_snap_country()

    def perform_destroy(self, instance):
        return country_usecases.DeleteCountryUseCase(
            country=self.get_object()
        ).execute()
