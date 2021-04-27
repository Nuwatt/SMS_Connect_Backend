from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.localize.filtersets import CountryFilter
from apps.localize.mixins import CountryMixin
from apps.localize.serializers import country_serializers
from apps.localize.usecases import country_usecases


class AddCountryView(CreateAPIView):
    """
    Use this end-point to add new country
    """
    serializer_class = country_serializers.AddCountrySerializer

    def perform_create(self, serializer):
        return country_usecases.AddCountryUseCase(
            serializer=serializer
        ).execute()


class ListCountryView(ListAPIView):
    """
    Use this end-point to list all country
    """
    serializer_class = country_serializers.ListCountrySerializer

    def get_queryset(self):
        return country_usecases.ListCountryUseCase().execute()


class UpdateCountryView(generics.UpdateAPIView, CountryMixin):
    """
    Use this end-point to update specific country
    """
    serializer_class = country_serializers.UpdateCountrySerializer

    def get_object(self):
        return self.get_country()

    def perform_update(self, serializer):
        return country_usecases.UpdateCountryUseCase(
            serializer=serializer,
            country=self.get_object()
        ).execute()


class DeleteCountryView(generics.DestroyAPIView, CountryMixin):
    """
    Use this end-point to delete specific country
    """

    def get_object(self):
        return self.get_country()

    def perform_destroy(self, instance):
        return country_usecases.DeleteCountryUseCase(
            country=self.get_object()
        ).execute()
