from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.core import generics
from apps.snap.filtersets import SnapStoreFilter
from apps.snap.mixins import SnapStoreMixin
from apps.snap.serializers import store_serializers
from apps.snap.usecases import store_usecases


class AddSnapStoreView(generics.CreateAPIView):
    """
    Use this end-point to add new store
    """
    serializer_class = store_serializers.AddSnapStoreSerializer

    def perform_create(self, serializer):
        return store_usecases.AddSnapStoreUseCase(
            serializer=serializer
        ).execute()


class ListSnapStoreView(generics.ListAPIView):
    """
    Use this end-point to list all store
    """
    filterset_class = SnapStoreFilter
    serializer_class = store_serializers.ListSnapStoreSerializer

    def get_queryset(self):
        return store_usecases.ListSnapStoreUseCase().execute()


class BasicListSnapStoreView(generics.ListAPIView):
    """
    Use this end-point to list all store
    """
    filterset_class = SnapStoreFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    serializer_class = store_serializers.BasicListSnapStoreSerializer

    def get_queryset(self):
        return store_usecases.ListSnapStoreUseCase().execute()


class UpdateSnapStoreView(generics.UpdateAPIView, SnapStoreMixin):
    """
    Use this end-point to update specific store
    """
    serializer_class = store_serializers.UpdateSnapStoreSerializer

    def get_object(self):
        return self.get_snap_store()

    def perform_update(self, serializer):
        return store_usecases.UpdateSnapStoreUseCase(
            serializer=serializer,
            snap_store=self.get_object()
        ).execute()


class DeleteSnapStoreView(generics.DestroyAPIView, SnapStoreMixin):
    """
    Use this end-point to delete specific store
    """

    def get_object(self):
        return self.get_snap_store()

    def perform_destroy(self, instance):
        return store_usecases.DeleteSnapStoreUseCase(
            snap_store=self.get_object()
        ).execute()
