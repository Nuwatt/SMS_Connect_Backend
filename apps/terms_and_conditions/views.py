from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.terms_and_conditions import serializers, usecases
from apps.terms_and_conditions.mixins import TermsAndConditionsMixin


class AddTermsAndConditionsView(CreateAPIView):
    """
    Use this end-point to add new terms and conditions
    """
    serializer_class = serializers.AddTermsAndConditionsSerializer

    def perform_create(self, serializer):
        return usecases.AddTermsAndConditionsUseCase(
            serializer=serializer
        ).execute()


class TermsAndConditionsDetailView(generics.RetrieveAPIView, TermsAndConditionsMixin):
    """
    Use this end-point to get terms and conditions
    """
    serializer_class = serializers.TermsAndConditionsDetailSerializer

    def get_object(self):
        return usecases.TermsAndConditionsDetailUseCase(
            terms_and_conditions=self.get_terms_and_conditions()
        ).execute()


class UpdateTermsAndConditionsView(generics.UpdateAPIView, TermsAndConditionsMixin):
    """
    Use this end-point to update specific terms and conditions
    """
    serializer_class = serializers.UpdateTermsAndConditionsSerializer

    def get_object(self):
        return self.get_terms_and_conditions()

    def perform_update(self, serializer):
        return usecases.UpdateTermsAndConditionsUseCase(
            serializer=serializer,
            terms_and_conditions=self.get_object()
        ).execute()


class DeleteTermsAndConditionsView(generics.DestroyAPIView, TermsAndConditionsMixin):
    """
    Use this end-point to delete specific terms and conditions
    """

    def get_object(self):
        return self.get_terms_and_conditions()

    def perform_destroy(self, instance):
        return usecases.DeleteTermsAndConditionsUseCase(
            terms_and_conditions=self.get_object()
        ).execute()
