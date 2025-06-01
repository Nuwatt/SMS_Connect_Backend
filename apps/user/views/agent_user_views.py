from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.core import generics
from apps.core.mixins import ResponseMixin
from apps.core.serializers import CSVFileInputSerializer
from apps.user import filtersets
from apps.user.mixins import AgentUserMixin
from apps.user.permissions import IsAgentUser, IsAdminPortalUser
from apps.user.serializers import agent_user_serializers
from apps.user.usecases import agent_user_usecases
from apps.user.views.azure_upload import AzureImageUploadView
from apps.user.permissions import IsAgentUser


class ListAgentUserView(generics.ListAPIView):
    """
    Use this end-point to list all agent user
    """
    serializer_class = agent_user_serializers.ListAgentUserSerializer
    filterset_class = filtersets.AgentUserFilter
    permission_classes = (IsAdminPortalUser,)

    def get_queryset(self):
        return agent_user_usecases.ListAgentUserUseCase().execute()


class RegisterAgentUserView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to register a new agent
    """
    serializer_class = agent_user_serializers.RegisterAgentUserSerializer
    permission_classes = (IsAdminPortalUser,)
    # permission_classes = [AllowAny]
    message = _('Registered successfully.')

    def perform_create(self, serializer):
        return agent_user_usecases.RegisterAgentUserUseCase(
            serializer=serializer
        ).execute()


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
    permission_classes = (IsAdminPortalUser,)

    def get_object(self):
        return self.get_agent_user()


class UpdateAgentUserView(generics.UpdateWithMessageAPIView, AgentUserMixin):
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


class AgentUserLoginView(generics.CreateAPIView, ResponseMixin):
    """
    Use this end-point to login and get access token for agent user
    """
    serializer_class = agent_user_serializers.AgentUserLoginSerializer
    response_serializer_class = agent_user_serializers.AgentUserLoginResponseSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return agent_user_usecases.AgentUserLoginUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        response = self.get_response_serializer(result)
        return Response(response.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: agent_user_serializers.AgentUserLoginResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UploadPortalUserAvatarView(generics.CreateAPIView, AgentUserMixin, ResponseMixin):
    """
    Use this end-point to upload avatar of a specific agent user
    """
    serializer_class = agent_user_serializers.UploadAgentUserAvatarSerializer
    response_serializer_class = agent_user_serializers.UploadAgentUserAvatarSerializer
    parser_classes = (MultiPartParser, JSONParser)

    def get_object(self):
        return self.get_agent_user()

    def perform_create(self, serializer):
        return agent_user_usecases.UploadAgentUserAvatarUseCase(
            agent_user=self.get_object(),
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        response_serializer = self.get_response_serializer(result.user)
        return Response(response_serializer.data)

    @swagger_auto_schema(responses={201: agent_user_serializers.UploadAgentUserAvatarSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImportAgentUserView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to import agent user from a csv file
    """
    serializer_class = CSVFileInputSerializer
    message = _('Agent User imported successfully.')
    parser_classes = (MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        return agent_user_usecases.ImportAgentUserUseCase(
            serializer=serializer
        ).execute()


class BasicListAgentUserView(generics.ListAPIView):
    """
    Use this end-point to list all agent with basic details
    """
    serializer_class = agent_user_serializers.BasicListAgentUserSerializer

    def get_queryset(self):
        return agent_user_usecases.BasicListAgentUserUseCase().execute()
    
class UploadImagesView(AzureImageUploadView):
    """
    POST /v1/user/agent-user/upload-images
    """
    # Require agent users?  Change as needed:
    permission_classes = (IsAgentUser,)
