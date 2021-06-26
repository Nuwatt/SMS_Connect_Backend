from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from apps.core import generics
from apps.core.serializers import IdCharSerializer, MessageResponseSerializer
from apps.questionnaire.mixins import QuestionnaireMixin
from apps.response import serializers, usecases
from apps.response.filtersets import ResponseFilter
from apps.response.mixins import ResponseMixin
from apps.user.mixins import AgentUserMixin
from apps.user.permissions import IsAgentUser, IsAdminPortalUser


class StartQuestionnaireView(generics.CreateAPIView, QuestionnaireMixin):
    """
    Use this end-point to start a questionnaire
    """
    serializer_class = serializers.StartQuestionnaireSerializer
    permission_classes = (IsAgentUser,)

    def get_object(self):
        return self.get_questionnaire()

    def perform_create(self, serializer):
        return usecases.StartQuestionnaireUseCase(
            questionnaire=self.get_object(),
            agent_user=self.request.user.agentuser,
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        return Response({
            'id': result.id
        })

    @swagger_auto_schema(responses={200: IdCharSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SummitQuestionnaireResponseView(generics.CreateAPIView, ResponseMixin):
    """
    Use this end-point to submit questionnaire's answers at once
    """
    serializer_class = serializers.BulkSummitQuestionnaireResponseSerializer
    permission_classes = (IsAgentUser,)

    def get_object(self):
        return self.get_response()

    def perform_create(self, serializer):
        usecases.SummitQuestionnaireResponseUseCase(
            response=self.get_object(),
            serializer=serializer
        ).execute()

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def response(self, result, serializer, status_code):
        return Response({
            'message': _('Submitted successfully.')
        })

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAgentResponseHistoryView(generics.ListAPIView):
    """
    Use this end-point to list all responses of a requesting agent user
    """
    serializer_class = serializers.ListAgentResponseHistorySerializer
    permission_classes = (IsAgentUser,)
    filterset_class = ResponseFilter

    def get_queryset(self):
        return usecases.ListAgentResponseHistoryUseCase(
            agent_user=self.request.user.agentuser
        ).execute()


class ListAgentResponseView(generics.ListAPIView, AgentUserMixin):
    """
    Use this end-point to list all responses of a specific agent
    """
    serializer_class = serializers.ListAgentResponseSerializer
    permission_classes = (IsAdminPortalUser,)

    def get_object(self):
        return self.get_agent_user()

    def get_queryset(self):
        return usecases.ListAgentResponseUseCase(
            agent_user=self.get_object()
        ).execute()


class ListQuestionnaireResponseView(generics.ListAPIView, QuestionnaireMixin):
    """
    Use this end-point to list response of a specific questionnaire
    """
    serializer_class = serializers.ListQuestionnaireResponseSerializer
    permission_classes = (IsAdminPortalUser,)

    def get_object(self):
        return self.get_questionnaire()

    def get_queryset(self):
        return usecases.ListQuestionnaireResponseUseCase(
            questionnaire=self.get_object()
        ).execute()


class ListResponseAnswerView(generics.ListAPIView, ResponseMixin):
    """
    Use this end-point to list answer of a specific response
    """
    serializer_class = serializers.ListQuestionnaireAnswerSerializer
    permission_classes = (IsAdminPortalUser,)

    def get_queryset(self):
        return usecases.ListResponseAnswerUseCase(
            response=self.get_response(),
        ).execute()
