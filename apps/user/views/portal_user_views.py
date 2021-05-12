from django.utils.translation import gettext_lazy as _

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.core import generics
from apps.core.mixins import ResponseMixin
from apps.core.serializers import MessageResponseSerializer
from apps.user.mixins import PortalUserMixin
from apps.user.serializers import portal_user_serializers
from apps.user.usecases import portal_user_usecases


class ListPortalUserView(generics.ListAPIView):
    """
    Use this end-point to list all portal user
    """
    serializer_class = portal_user_serializers.ListPortalUserSerializer

    def get_queryset(self):
        return portal_user_usecases.ListPortalUserUseCase().execute()


class RegisterPortalUserView(generics.CreateAPIView):
    """
    Use this end-point to register a new Portal user
    """
    serializer_class = portal_user_serializers.RegisterPortalUserSerializer

    def perform_create(self, serializer):
        return portal_user_usecases.RegisterPortalUserUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        return Response({
            'message': _('Registered successfully.')
        })

    @swagger_auto_schema(responses={201: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PortalUserDetailView(generics.RetrieveAPIView, PortalUserMixin):
    """
    Use this end-point to get detail of a specific portal user
    """
    serializer_class = portal_user_serializers.PortalUserDetailSerializer

    def get_object(self):
        return self.get_portal_user()


class UpdatePortalUserView(generics.UpdateAPIView, PortalUserMixin):
    """
    Use this end-point to update specific portal user detail
    """
    serializer_class = portal_user_serializers.UpdatePortalUserSerializer

    def get_object(self):
        return self.get_portal_user()

    def perform_update(self, serializer):
        return portal_user_usecases.UpdatePortalUserUseCase(
            portal_user=self.get_object(),
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


class DeletePortalUserView(generics.DestroyAPIView, PortalUserMixin):
    """
    Use this end-point to delete a specific portal user
    """

    def get_object(self):
        return self.get_portal_user()

    def perform_destroy(self, instance):
        return portal_user_usecases.DeletePortalUserUseCase(
            portal_user=self.get_object()
        ).execute()


class PortalUserLoginView(generics.CreateAPIView, ResponseMixin):
    """
    Use this end-point to login and get access token for portal user
    """
    serializer_class = portal_user_serializers.PortalUserLoginSerializer
    response_serializer_class = portal_user_serializers.PortalUserLoginResponseSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return portal_user_usecases.PortalUserLoginUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        response = self.get_response_serializer(result)
        return Response(response.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: portal_user_serializers.PortalUserLoginResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UploadPortalUserAvatarView(generics.CreateAPIView, PortalUserMixin):
    """
    Use this end-point to upload avatar of a specific portal user
    """
    serializer_class = portal_user_serializers.UploadPortalUserAvatarSerializer

    def get_object(self):
        return self.get_portal_user()

    def perform_create(self, serializer):
        return portal_user_usecases.UploadPortalUserAvatarUseCase(
            portal_user=self.get_object(),
            serializer=serializer
        ).execute()
