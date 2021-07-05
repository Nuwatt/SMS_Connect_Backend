from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response

from apps.core import generics
from apps.core.serializers import MessageResponseSerializer
from apps.question.filtersets import QuestionFilter
from apps.question.mixins import QuestionMixin
from apps.question.serializers import question_serializers
from apps.question.usecases import question_usecases
from apps.questionnaire.mixins import QuestionnaireMixin
from apps.user.permissions import IsAgentUser


class AddQuestionView(generics.CreateWithMessageAPIView, QuestionnaireMixin):
    """
    Use this end-point to add new question
    """
    serializer_class = question_serializers.AddQuestionSerializer
    message = _('Question added successfully.')

    def perform_create(self, serializer):
        return question_usecases.AddQuestionUseCase(
            questionnaire=self.get_questionnaire(),
            serializer=serializer
        ).execute()


class BulkAddQuestionView(generics.CreateWithMessageAPIView, QuestionnaireMixin):
    """
    Use this end-point to add new question in bulk
    """
    serializer_class = question_serializers.BulkAddQuestionSerializer
    message = _('Question added successfully.')

    def perform_create(self, serializer):
        return question_usecases.BulkAddQuestionUseCase(
            questionnaire=self.get_questionnaire(),
            serializer=serializer
        ).execute()


class ListQuestionView(generics.ListAPIView):
    """
    Use this end-point to list all questions
    """
    filterset_class = QuestionFilter
    serializer_class = question_serializers.ListQuestionForAgentUserSerializer

    def get_queryset(self):
        return question_usecases.ListQuestionUseCase().execute()


class QuestionDetailView(generics.RetrieveAPIView, QuestionMixin):
    """
    Use this end-point to get detail of a specific question
    """
    serializer_class = question_serializers.QuestionDetailSerializer

    def get_object(self):
        return self.get_question()


class ImportQuestionView(generics.CreateWithMessageAPIView, QuestionnaireMixin):
    """
    Use this end-point to import questions in the form of csv file
    """
    serializer_class = question_serializers.ImportQuestionSerializer
    message = _('Question imported successfully.')

    def get_object(self):
        return self.get_questionnaire()

    def perform_create(self, serializer):
        return question_usecases.ImportQuestionUseCase(
            serializer=serializer,
            questionnaire=self.get_object()
        ).execute()


class ExportQuestionView(generics.GenericAPIView, QuestionnaireMixin):
    """
    Use this end-point to export questions to csv file
    """

    def get_object(self):
        return self.get_questionnaire()

    def get(self, *args, **kwargs):
        return question_usecases.ExportQuestionUseCase(
            questionnaire=self.get_object()
        ).execute()


class ListQuestionForAgentView(generics.ListAPIView, QuestionnaireMixin):
    """
    Use this end-point to list all question of a specific questionnaire for an agent user only
    """
    permission_classes = (IsAgentUser,)
    serializer_class = question_serializers.ListQuestionForAgentUserSerializer

    def get_object(self):
        return self.get_questionnaire()

    def get_queryset(self):
        return question_usecases.ListQuestionForAgentUseCase(
            agent_user=self.request.user.agentuser,
            questionnaire=self.get_object()
        ).execute()


class DeleteQuestionView(generics.DestroyAPIView, QuestionMixin):
    """
    Use this end-point to delete specific question
    """

    def get_object(self):
        return self.get_question()

    def perform_destroy(self, instance):
        return question_usecases.DeleteQuestionUseCase(
            question=self.get_object()
        ).execute()


class UpdateQuestionView(generics.UpdateAPIView, QuestionMixin):
    """
    Use this end-point to update specific question
    """
    serializer_class = question_serializers.UpdateQuestionSerializer

    def get_object(self):
        return self.get_question()

    def perform_update(self, serializer):
        return question_usecases.UpdateQuestionUseCase(
            serializer=serializer,
            question=self.get_object()
        ).execute()
