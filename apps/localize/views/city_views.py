from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.core import generics
from apps.localize.filtersets import CityFilter
from apps.localize.mixins import CityMixin
from apps.localize.serializers import city_serializers
from apps.localize.usecases import city_usecases


class AddCityView(generics.CreateAPIView):
    """
    Use this end-point to add new city
    """
    serializer_class = city_serializers.AddCitySerializer

    def perform_create(self, serializer):
        return city_usecases.AddCityUseCase(
            serializer=serializer
        ).execute()


class ListCityView(generics.ListAPIView):
    """
    Use this end-point to list all cities
    """
    serializer_class = city_serializers.ListCitySerializer
    filterset_class = CityFilter

    def get_queryset(self):
        return city_usecases.ListCityUseCase().execute()

    # @method_decorator(cache_page(60 * 60 * 2))
    # @method_decorator(vary_on_headers("Authorization", ))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateCityView(generics.UpdateAPIView, CityMixin):
    """
    Use this end-point to update specific city
    """
    serializer_class = city_serializers.UpdateCitySerializer

    def get_object(self):
        return self.get_city()

    def perform_update(self, serializer):
        return city_usecases.UpdateCityUseCase(
            serializer=serializer,
            city=self.get_object()
        ).execute()


class DeleteCityView(generics.DestroyAPIView, CityMixin):
    """
    Use this end-point to delete specific city
    """

    def get_object(self):
        return self.get_city()

    def perform_destroy(self, instance):
        return city_usecases.DeleteCityUseCase(
            city=self.get_object()
        ).execute()
