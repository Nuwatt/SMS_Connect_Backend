from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.questionnaire.filtersets import QuestionnaireFilter
from apps.questionnaire.mixins import QuestionnaireMixin
from apps.questionnaire.serializers import questionnaire_serializers
from apps.questionnaire.usecases import questionnaire_usecases


class AddQuestionnaireView(CreateAPIView):
    """
    Use this end-point to add new questionnaire
    """
    serializer_class = questionnaire_serializers.AddQuestionnaireSerializer

    def perform_create(self, serializer):
        return questionnaire_usecases.AddQuestionnaireUseCase(
            serializer=serializer
        ).execute()


class ListQuestionnaireView(ListAPIView):
    """
    Use this end-point to list all questionnaire
    """
    serializer_class = questionnaire_serializers.ListQuestionnaireSerializer
    filterset_class = QuestionnaireFilter

    def get_queryset(self):
        return questionnaire_usecases.ListQuestionnaireUseCase().execute()


class UpdateQuestionnaireView(generics.UpdateAPIView, QuestionnaireMixin):
    """
    Use this end-point to update specific questionnaire
    """
    serializer_class = questionnaire_serializers.UpdateQuestionnaireSerializer

    def get_object(self):
        return self.get_questionnaire()

    def perform_update(self, serializer):
        return questionnaire_usecases.UpdateQuestionnaireUseCase(
            serializer=serializer,
            questionnaire=self.get_object()
        ).execute()


class DeleteQuestionnaireView(generics.DestroyAPIView, QuestionnaireMixin):
    """
    Use this end-point to delete specific questionnaire
    """

    def get_object(self):
        return self.get_questionnaire()

    def perform_destroy(self, instance):
        return questionnaire_usecases.DeleteQuestionnaireUseCase(
            questionnaire=self.get_object()
        ).execute()
