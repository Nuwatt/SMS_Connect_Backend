from apps.core import generics
from apps.question.filtersets import QuestionTypeFilter
from apps.question.serializers import question_type_serializers
from apps.question.usecases import question_type_usecases


class AddQuestionView(generics.CreateAPIView):
    """
    Use this end-point to add new question type
    """
    serializer_class = question_type_serializers.AddQuestionTypeSerializer

    def perform_create(self, serializer):
        return question_type_usecases.AddQuestionTypeUseCase(
            serializer=serializer
        ).execute()


class ListQuestionView(generics.ListAPIView):
    """
    Use this end-point to list all question types
    """
    serializer_class = question_type_serializers.ListQuestionTypeSerializer
    filterset_class = QuestionTypeFilter

    def get_queryset(self):
        return question_type_usecases.ListQuestionTypeUseCase().execute()
