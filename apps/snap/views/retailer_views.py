from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


from apps.core import generics
from apps.snap.filtersets import SnapRetailerFilter
from apps.snap.mixins import SnapRetailerMixin
from apps.snap.serializers import retailer_serializers
from apps.snap.usecases import retailer_usecases


class AddSnapRetailerView(generics.CreateAPIView):
    """
    Use this end-point to add new retailer
    """
    serializer_class = retailer_serializers.AddSnapRetailerSerializer

    def perform_create(self, serializer):
        return retailer_usecases.AddSnapRetailerUseCase(
            serializer=serializer
        ).execute()


class ListSnapRetailerView(generics.ListAPIView):
    """
    Use this end-point to list all retailer
    """
    serializer_class = retailer_serializers.ListSnapRetailerSerializer
    filterset_class = SnapRetailerFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return retailer_usecases.ListSnapRetailerUseCase().execute()


class BasicListSnapRetailerView(generics.ListAPIView):
    """
    Use this end-point to list all retailer with basic list
    """
    serializer_class = retailer_serializers.BasicListSnapRetailerSerializer
    filterset_class = SnapRetailerFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return retailer_usecases.BasicListSnapRetailerUseCase().execute()


class UpdateSnapRetailerView(generics.UpdateAPIView, SnapRetailerMixin):
    """
    Use this end-point to update specific retailer
    """
    serializer_class = retailer_serializers.UpdateSnapRetailerSerializer

    def get_object(self):
        return self.get_snap_retailer()

    def perform_update(self, serializer):
        return retailer_usecases.UpdateSnapRetailerUseCase(
            serializer=serializer,
            snap_retailer=self.get_object()
        ).execute()


class DeleteSnapRetailerView(generics.DestroyAPIView, SnapRetailerMixin):
    """
    Use this end-point to delete specific retailer
    """

    def get_object(self):
        return self.get_snap_retailer()

    def perform_destroy(self, instance):
        return retailer_usecases.DeleteSnapRetailerUseCase(
            snap_retailer=self.get_object()
        ).execute()

