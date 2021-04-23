from django.utils.translation import gettext_lazy as _

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from apps.core.generics import ListAPIView, CreateAPIView
from apps.core.serializers import MessageResponseSerializer
from apps.user.serializers import portal_user_serializers
from apps.user.usecases import portal_user_usecases


class ListPortalUserView(ListAPIView):
    """
    Use this end-point to list all portal user
    """
    serializer_class = portal_user_serializers.ListPortalUserSerializer

    def get_queryset(self):
        return portal_user_usecases.ListPortalUserUseCase().execute()


class RegisterPortalUserView(CreateAPIView):
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
