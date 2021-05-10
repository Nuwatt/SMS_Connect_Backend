from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from apps.core import generics
from apps.core.serializers import MessageResponseSerializer
from apps.user.mixins import AgentUserMixin
from apps.user.permissions import IsAgentUser
from apps.user.serializers import agent_user_serializers
from apps.user.usecases import agent_user_usecases


class ListAgentUserView(generics.ListAPIView):
    """
    Use this end-point to list all agent user
    """
    serializer_class = agent_user_serializers.ListAgentUserSerializer

    def get_queryset(self):
        return agent_user_usecases.ListAgentUserUseCase().execute()


class RegisterAgentUserView(generics.CreateAPIView):
    """
    Use this end-point to register a new agent
    """
    serializer_class = agent_user_serializers.RegisterAgentUserSerializer

    def perform_create(self, serializer):
        return agent_user_usecases.RegisterAgentUserUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        return Response({
            'message': _('Registered successfully.')
        })

    @swagger_auto_schema(responses={201: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AgentUserProfileView(generics.RetrieveAPIView):
    """
    Use this end-point to get agent profile
    """
    serializer_class = agent_user_serializers.AgentUserProfileSerializer
    permission_classes = (IsAgentUser,)

    def get_object(self):
        return self.request.user


class UpdateAgentUserProfileView(generics.UpdateAPIView):
    """
    Use this end-point to update own agent user profile
    """
    serializer_class = agent_user_serializers.UpdateAgentUserProfileSerializer
    permission_classes = (IsAgentUser,)

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        return agent_user_usecases.UpdateAgentUserProfile(
            user=self.get_object(),
            serializer=serializer
        ).execute()


class AgentUserDetailView(generics.RetrieveAPIView, AgentUserMixin):
    """
    Use this end-point to get detail of a specific agent user
    """
    serializer_class = agent_user_serializers.AgentUserDetailSerializer

    def get_object(self):
        return self.get_agent_user()


class UpdateAgentUserView(generics.UpdateAPIView, AgentUserMixin):
    """
    Use this end-point to update specific agent user detail
    """
    serializer_class = agent_user_serializers.UpdateAgentUserSerializer

    def get_object(self):
        return self.get_agent_user()

    def perform_update(self, serializer):
        return agent_user_usecases.UpdateAgentUserUseCase(
            agent_user=self.get_object(),
            serializer=serializer
        ).execute()

    def response(self, serializer):
        return Response({
            'message': _('Updated successfully.')
        })

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DeleteAgentUserView(generics.DestroyAPIView, AgentUserMixin):
    """
    Use this end-point to delete a specific agent user
    """

    def get_object(self):
        return self.get_agent_user()

    def perform_destroy(self, instance):
        return agent_user_usecases.DeleteAgentUserUseCase(
            agent_user=self.get_object()
        ).execute()
