from rest_framework import serializers

from apps.snap.models import SnapChannel


class SnapChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapChannel
        fields = '__all__'


class AddSnapChannelSerializer(SnapChannelSerializer):
    class Meta(SnapChannelSerializer.Meta):
        fields = (
            'name',
        )


class ListSnapChannelSerializer(SnapChannelSerializer):
    class Meta(SnapChannelSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateSnapChannelSerializer(AddSnapChannelSerializer):
    pass
