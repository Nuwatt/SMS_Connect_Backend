from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from rest_framework.response import Response

from apps.core.generics import ListAPIView, CreateAPIView
from apps.core.serializers import MessageResponseSerializer
from apps.question.mixins import QuestionTypeMixin
from apps.question.serializers import question_type_serializers
from apps.question.usecases import question_type_usecases


class AddQuestionView(CreateAPIView):
    """
    Use this end-point to add new question type
    """
    serializer_class = question_type_serializers.AddQuestionTypeSerializer

    def perform_create(self, serializer):
        return question_type_usecases.AddQuestionTypeUseCase(
            serializer=serializer
        ).execute()


class ListQuestionView(ListAPIView):
    """
    Use this end-point to list all question types
    """
    serializer_class = question_type_serializers.ListQuestionTypeSerializer

    def get_queryset(self):
        return question_type_usecases.ListQuestionTypeUseCase().execute()
