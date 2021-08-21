from rest_framework.filters import OrderingFilter

from apps.core import generics
from apps.snap.mixins import SnapChannelMixin
from apps.snap.serializers import channel_serializers
from apps.snap.usecases import channel_usecases


class AddSnapChannelView(generics.CreateAPIView):
    """
    Use this end-point to add new snap channel
    """
    serializer_class = channel_serializers.AddSnapChannelSerializer

    def perform_create(self, serializer):
        return channel_usecases.AddSnapChannelUseCase(
            serializer=serializer
        ).execute()


class ListSnapChannelView(generics.ListAPIView):
    """
    Use this end-point to list all snap channel
    """
    serializer_class = channel_serializers.ListSnapChannelSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return channel_usecases.ListSnapChannelUseCase().execute()


class UpdateSnapChannelView(generics.UpdateAPIView, SnapChannelMixin):
    """
    Use this end-point to update specific snap channel
    """
    serializer_class = channel_serializers.UpdateSnapChannelSerializer

    def get_object(self):
        return self.get_snap_channel()

    def perform_update(self, serializer):
        return channel_usecases.UpdateSnapChannelUseCase(
            serializer=serializer,
            snap_channel=self.get_object()
        ).execute()


class DeleteSnapChannelView(generics.DestroyAPIView, SnapChannelMixin):
    """
    Use this end-point to delete specific snap channel
    """

    def get_object(self):
        return self.get_snap_channel()

    def perform_destroy(self, instance):
        return channel_usecases.DeleteSnapChannelUseCase(
            snap_channel=self.get_object()
        ).execute()
