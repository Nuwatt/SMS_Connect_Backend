from rest_framework.permissions import AllowAny

from apps.core import generics
from apps.user.serializers import base_serializers
from apps.user.usecases import base_usecases


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
