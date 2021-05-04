from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from rest_framework.response import Response

from apps.core.generics import ListAPIView, CreateAPIView
from apps.core.serializers import MessageResponseSerializer
from apps.question.filtersets import QuestionFilter
from apps.question.mixins import QuestionMixin
from apps.question.serializers import question_serializers
from apps.question.usecases import question_usecases
from apps.questionnaire.mixins import QuestionnaireMixin


class AddQuestionView(CreateAPIView, QuestionnaireMixin):
    """
    Use this end-point to add new question
    """
    serializer_class = question_serializers.AddQuestionSerializer

    def perform_create(self, serializer):
        return question_usecases.AddQuestionUseCase(
            questionnaire=self.get_questionnaire(),
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        return Response({
            'message': _('Question added successfully.')
        }, status=status_code)

    @swagger_auto_schema(responses={201: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListQuestionView(ListAPIView):
    """
    Use this end-point to list all questions
    """
    serializer_class = question_serializers.ListQuestionSerializer
    filterset_class = QuestionFilter

    def get_queryset(self):
        return question_usecases.ListQuestionUseCase().execute()


class QuestionDetailView(generics.RetrieveAPIView, QuestionMixin):
    """
    Use this end-point to get detail of a specific question
    """
    serializer_class = question_serializers.QuestionDetailSerializer

    def get_object(self):
        return self.get_question()
