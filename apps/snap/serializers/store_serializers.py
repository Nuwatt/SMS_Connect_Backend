from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.snap.models import SnapStore, SnapChannel


class SnapStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapStore
        fields = '__all__'


class AddStoreRetailerSerializer(SnapStoreSerializer):
    # for adding store and retailer
    channel = serializers.PrimaryKeyRelatedField(queryset=SnapChannel.objects.unarchived())
    retailer = serializers.CharField()

    class Meta(SnapStoreSerializer.Meta):
        fields = (
            'name',
            'channel',
            'retailer',
            'city'
        )


class AddSnapStoreSerializer(SnapStoreSerializer):
    name = serializers.ListSerializer(child=serializers.CharField())

    class Meta(SnapStoreSerializer.Meta):
        fields = (
            'name',
            'retailer',
            'channel',
            'city',
        )

    default_error_messages = {
        'empty_name': _('Requires in list.')
    }

    def validate_name(self, data):
        if len(data) == 0:
            self.fail('empty_name')
        return data


class ListSnapStoreSerializer(SnapStoreSerializer):
    retailer = IdNameSerializer()
    city = IdNameSerializer()
    channel = IdNameSerializer()
    country = IdNameSerializer(source='city.country', allow_null=True)

    class Meta(SnapStoreSerializer.Meta):
        fields = (
            'id',
            'retailer',
            'channel',
            'name',
            'city',
            'country',
        )


class BasicListSnapStoreSerializer(SnapStoreSerializer):
    class Meta(SnapStoreSerializer.Meta):
        fields = (
            'id',
            'name'
        )


class ListStoreForAgentUserSerializer(SnapStoreSerializer):
    retailer = IdNameSerializer()

    class Meta(SnapStoreSerializer.Meta):
        fields = (
            'id',
            'retailer',
            'name',
        )


class UpdateSnapStoreSerializer(SnapStoreSerializer):
    class Meta(SnapStoreSerializer.Meta):
        fields = (
            'name',
            'retailer',
            'channel',
            'city'
        )
