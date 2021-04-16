from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.core import generics
from apps.core.mixins import ResponseMixin
from apps.user import serializers, usecases


class UserSignupView(generics.CreateAPIView):
    """
    Use this end-point to signup
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSignupSerializer

    def perform_create(self, serializer):
        return usecases.UserSignupUseCase(
            serializer=serializer
        ).execute()


class UserLoginView(generics.CreateAPIView, ResponseMixin):
    """
    Use this end-point to login and get access token
    """
    serializer_class = serializers.UserLoginSerializer
    response_serializer_class = serializers.UserLoginResponseSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        return usecases.UserLoginUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, status_code):
        response = self.get_response_serializer(result)
        return Response(response.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: serializers.UserLoginResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListUserView(generics.ListAPIView):
    """
    Use this end-point to list all users in the system
    """
    serializer_class = serializers.ListUserSerializer

    def get_queryset(self):
        return usecases.ListUserUseCase().execute()
