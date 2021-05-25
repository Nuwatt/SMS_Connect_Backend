from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from apps.core import generics
from apps.localize.filtersets import CountryFilter
from apps.localize.mixins import CountryMixin
from apps.localize.serializers import country_serializers
from apps.localize.usecases import country_usecases


class AddCountryView(generics.CreateAPIView):
    """
    Use this end-point to add new country
    """
    serializer_class = country_serializers.AddCountrySerializer

    def perform_create(self, serializer):
        return country_usecases.AddCountryUseCase(
            serializer=serializer
        ).execute()


class ListCountryView(generics.ListAPIView):
    """
    Use this end-point to list all country
    """
    serializer_class = country_serializers.ListCountrySerializer
    filterset_class = CountryFilter

    def get_queryset(self):
        return country_usecases.ListCountryUseCase().execute()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListNationalityView(generics.ListAPIView):
    """
    Use this end-point to list all nationality
    """
    serializer_class = country_serializers.ListNationalitySerializer
    filterset_class = CountryFilter

    def get_queryset(self):
        return country_usecases.ListNationalityUseCase().execute()


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
