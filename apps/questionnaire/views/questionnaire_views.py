from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from apps.core import generics
from apps.core.serializers import IdCharSerializer
from apps.questionnaire.filtersets import QuestionnaireFilter, AvailableQuestionnaireForAgentFilter
from apps.questionnaire.mixins import QuestionnaireMixin
from apps.questionnaire.serializers import questionnaire_serializers
from apps.questionnaire.usecases import questionnaire_usecases
from apps.user.permissions import IsAgentUser


class AddQuestionnaireView(generics.CreateAPIView):
    """
    Use this end-point to add new questionnaire
    """
    serializer_class = questionnaire_serializers.AddQuestionnaireSerializer

    def perform_create(self, serializer):
        return questionnaire_usecases.AddQuestionnaireUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        return Response({
            'id': result.id
        })

    @swagger_auto_schema(responses={201: IdCharSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListQuestionnaireView(generics.ListAPIView):
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


class QuestionnaireDetailView(generics.RetrieveAPIView, QuestionnaireMixin):
    """
    Use this end-point to get detail of specific questionnaire
    """
    serializer_class = questionnaire_serializers.QuestionnaireDetailSerializer

    def get_object(self):
        return self.get_questionnaire()


class ListAvailableQuestionnaireForAgentView(generics.ListAPIView):
    """
    Use this end-point to list available questionnaire for a requesting agent-user
    """
    permission_classes = (IsAgentUser,)
    filterset_class = AvailableQuestionnaireForAgentFilter

    serializer_class = questionnaire_serializers.ListAvailableQuestionnaireForAgentSerializer

    def get_queryset(self):
        return questionnaire_usecases.ListAvailableQuestionnaireForAgentUseCase(
            agent_user=self.request.user.agentuser
        ).execute()
