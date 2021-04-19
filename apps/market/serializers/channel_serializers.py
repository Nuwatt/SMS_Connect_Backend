from rest_framework import serializers

from apps.market.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class AddChannelSerializer(ChannelSerializer):
    class Meta(ChannelSerializer.Meta):
        fields = (
            'name',
        )


class ListChannelSerializer(ChannelSerializer):
    class Meta(ChannelSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateChannelSerializer(AddChannelSerializer):
    pass
