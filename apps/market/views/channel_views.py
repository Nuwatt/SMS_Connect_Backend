from rest_framework import generics

from apps.core.generics import CreateAPIView, ListAPIView
from apps.market.mixins import ChannelMixin
from apps.market.serializers import channel_serializers
from apps.market.usecases import channel_usecases


class AddChannelView(CreateAPIView):
    """
    Use this end-point to add new channel
    """
    serializer_class = channel_serializers.AddChannelSerializer

    def perform_create(self, serializer):
        return channel_usecases.AddChannelUseCase(
            serializer=serializer
        ).execute()


class ListChannelView(ListAPIView):
    """
    Use this end-point to list all channel
    """
    serializer_class = channel_serializers.ListChannelSerializer

    def get_queryset(self):
        return channel_usecases.ListChannelUseCase().execute()


class UpdateChannelView(generics.UpdateAPIView, ChannelMixin):
    """
    Use this end-point to update specific channel
    """
    serializer_class = channel_serializers.UpdateChannelSerializer

    def get_object(self):
        return self.get_channel()

    def perform_update(self, serializer):
        return channel_usecases.UpdateChannelUseCase(
            serializer=serializer,
            store=self.get_object()
        ).execute()


class DeleteChannelView(generics.DestroyAPIView, ChannelMixin):
    """
    Use this end-point to delete specific channel
    """

    def get_object(self):
        return self.get_channel()

    def perform_destroy(self, instance):
        return channel_usecases.DeleteChannelUseCase(
            store=self.get_object()
        ).execute()
