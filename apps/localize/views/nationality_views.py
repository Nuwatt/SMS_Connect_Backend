from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.localize.mixins import NationalityMixin
from apps.localize.serializers import nationality_serializers
from apps.localize.usecases import nationality_usecases


class AddNationalityView(CreateAPIView):
    """
    Use this end-point to add new nationality
    """
    serializer_class = nationality_serializers.AddNationalitySerializer

    def perform_create(self, serializer):
        return nationality_usecases.AddNationalityUseCase(
            serializer=serializer
        ).execute()


class ListNationalityView(ListAPIView):
    """
    Use this end-point to list all nationality
    """
    serializer_class = nationality_serializers.ListNationalitySerializer

    def get_queryset(self):
        return nationality_usecases.ListNationalityUseCase().execute()


class UpdateNationalityView(generics.UpdateAPIView, NationalityMixin):
    """
    Use this end-point to update specific nationality
    """
    serializer_class = nationality_serializers.UpdateNationalitySerializer

    def get_object(self):
        return self.get_nationality()

    def perform_update(self, serializer):
        return nationality_usecases.UpdateNationalityUseCase(
            serializer=serializer,
            nationality=self.get_object()
        ).execute()


class DeleteNationalityView(generics.DestroyAPIView, NationalityMixin):
    """
    Use this end-point to delete specific nationality
    """

    def get_object(self):
        return self.get_nationality()

    def perform_destroy(self, instance):
        return nationality_usecases.DeleteNationalityUseCase(
            nationality=self.get_object()
        ).execute()
