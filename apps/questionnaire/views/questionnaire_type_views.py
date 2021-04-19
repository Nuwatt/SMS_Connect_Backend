from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.questionnaire.mixins import QuestionnaireTypeMixin
from apps.questionnaire.serializers import questionnaire_type_serializers
from apps.questionnaire.usecases import questionnaire_type_usecases


class AddQuestionnaireTypeView(CreateAPIView):
    """
    Use this end-point to add new questionnaire type
    """
    serializer_class = questionnaire_type_serializers.AddQuestionnaireTypeSerializer

    def perform_create(self, serializer):
        return questionnaire_type_usecases.AddQuestionnaireTypeUseCase(
            serializer=serializer
        ).execute()


class ListQuestionnaireTypeView(ListAPIView):
    """
    Use this end-point to list all questionnaire type
    """
    serializer_class = questionnaire_type_serializers.ListQuestionnaireTypeSerializer

    def get_queryset(self):
        return questionnaire_type_usecases.ListQuestionnaireTypeUseCase().execute()


class UpdateQuestionnaireTypeView(generics.UpdateAPIView, QuestionnaireTypeMixin):
    """
    Use this end-point to update specific questionnaire type
    """
    serializer_class = questionnaire_type_serializers.UpdateQuestionnaireTypeSerializer

    def get_object(self):
        return self.get_questionnaire_type()

    def perform_update(self, serializer):
        return questionnaire_type_usecases.UpdateQuestionnaireTypeUseCase(
            serializer=serializer,
            questionnaire_type=self.get_object()
        ).execute()


class DeleteQuestionnaireTypeView(generics.DestroyAPIView, QuestionnaireTypeMixin):
    """
    Use this end-point to delete specific questionnaire type
    """

    def get_object(self):
        return self.get_questionnaire_type()

    def perform_destroy(self, instance):
        return questionnaire_type_usecases.DeleteQuestionnaireTypeUseCase(
            questionnaire_type=self.get_object()
        ).execute()
