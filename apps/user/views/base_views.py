from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.core import generics
from apps.core.mixins import ResponseMixin
from apps.user.serializers import base_serializers
from apps.user.usecases import base_usecases


class UserLoginView(generics.CreateAPIView, ResponseMixin):
    """
    Use this end-point to login and get access token
    """
    serializer_class = base_serializers.UserLoginSerializer
    response_serializer_class = base_serializers.UserLoginResponseSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return base_usecases.UserLoginUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        response = self.get_response_serializer(result)
        return Response(response.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: base_serializers.UserLoginResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PasswordResetView(generics.CreateAPIView):
    """
    Use this end-point to reset password
    """
    serializer_class = base_serializers.PasswordResetSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return base_usecases.ResetPasswordBaseUseCase(
            serializer=serializer
        ).execute()


class PasswordResetConfirmView(generics.CreateAPIView):
    """
    Use this end-point to confirm reset password
    """
    serializer_class = base_serializers.PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return base_usecases.ResetPasswordConfirmBaseUseCase(
            serializer=serializer
        ).execute()


class ChangePasswordView(generics.CreateAPIView):
    """
    Use this end-point to change password
    """
    serializer_class = base_serializers.ChangePasswordSerializer

    def perform_create(self, serializer):
        return base_usecases.ChangePasswordUseCase(
            user=self.request.user,
            serializer=serializer
        ).execute()


class SupportView(generics.CreateAPIView):
    """
    Use this end-point to send support email to inception
    """
    serializer_class = base_serializers.SupportSerializer

    def perform_create(self, serializer):
        base_usecases.SupportUseCase(
            user=self.request.user,
            serializer=serializer
        ).execute()
