from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response

from apps.core import generics
from apps.core.serializers import MessageResponseSerializer
from apps.market.mixins import RetailerMixin
from apps.market.serializers import retailer_serializers
from apps.market.usecases import retailer_usecases


class AddRetailerView(generics.CreateAPIView):
    """
    Use this end-point to add new retailer
    """
    serializer_class = retailer_serializers.AddRetailerSerializer

    def perform_create(self, serializer):
        return retailer_usecases.AddRetailerUseCase(
            serializer=serializer
        ).execute()


class ListRetailerView(generics.ListAPIView):
    """
    Use this end-point to list all retailer
    """
    serializer_class = retailer_serializers.ListRetailerSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_agent_user:
            return retailer_usecases.ListRetailerForAgentUserUseCase(
                agent_user=user.agentuser
            ).execute()
        return retailer_usecases.ListRetailerUseCase().execute()


class UpdateRetailerView(generics.UpdateAPIView, RetailerMixin):
    """
    Use this end-point to update specific retailer
    """
    serializer_class = retailer_serializers.UpdateRetailerSerializer

    def get_object(self):
        return self.get_retailer()

    def perform_update(self, serializer):
        return retailer_usecases.UpdateRetailerUseCase(
            serializer=serializer,
            retailer=self.get_object()
        ).execute()


class DeleteRetailerView(generics.DestroyAPIView, RetailerMixin):
    """
    Use this end-point to delete specific retailer
    """

    def get_object(self):
        return self.get_retailer()

    def perform_destroy(self, instance):
        return retailer_usecases.DeleteRetailerUseCase(
            retailer=self.get_object()
        ).execute()


class ImportRetailerView(generics.CreateAPIView):
    """
    Use this end-point to import retailer from csv format
    """
    serializer_class = retailer_serializers.ImportRetailerSerializer

    def perform_create(self, serializer):
        return retailer_usecases.ImportRetailerUseCase(
            serializer=serializer
        ).execute()

    def response(self, result, serializer, status_code):
        return Response({
            'message': _('Imported and saved successfully.')
        })

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
