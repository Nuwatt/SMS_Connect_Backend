from django.utils.translation import gettext_lazy as _

from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase

from apps.core import generics
from apps.core.serializers import MessageResponseSerializer
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

    def response(self, result, serializer, status_code):
        return Response({
            'message': _('Password changed successfully.')
        })

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class TokenVerifyView(TokenViewBase):
    """
    Takes a token and indicates if it is valid.  This view provides no
    information about a token's fitness for a particular use.
    """
    serializer_class = base_serializers.TokenVerifySerializer
