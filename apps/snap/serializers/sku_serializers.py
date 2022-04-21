from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.core.serializers import IdNameCharSerializer, IdNameSerializer
from apps.snap.models import SnapSKU


class SnapSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapSKU
        fields = '__all__'


class AddSnapSKUSerializer(SnapSKUSerializer):
    name = serializers.ListSerializer(child=serializers.CharField())

    default_error_messages = {
        'empty_name': _('Requires in list.')
    }

    class Meta(SnapSKUSerializer.Meta):
        fields = (
            'name',
            'brand',
            'category',
        )

    def validate_name(self, data):
        if len(data) == 0:
            self.fail('empty_name')
        return data


class ListSnapSKUSerializer(SnapSKUSerializer):
    category = IdNameCharSerializer()
    brand = IdNameCharSerializer()

    class Meta(SnapSKUSerializer.Meta):
        fields = (
            'id',
            'name',
            'category',
            'brand',
        )


class UpdateSnapSKUSerializer(SnapSKUSerializer):
    class Meta(SnapSKUSerializer.Meta):
        fields = (
            'name',
            'brand',
            'category',
        )
