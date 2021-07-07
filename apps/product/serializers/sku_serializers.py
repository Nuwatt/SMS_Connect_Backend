from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.core.serializers import CSVFileInputSerializer, IdNameCharSerializer, IdNameSerializer
from apps.product.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'


class AddSKUSerializer(SKUSerializer):
    name = serializers.ListSerializer(child=serializers.CharField())

    default_error_messages = {
        'empty_name': _('Requires in list.')
    }

    class Meta(SKUSerializer.Meta):
        fields = (
            'name',
            'brand',
            'category',
            'country'
        )

    def validate_name(self, data):
        if len(data) == 0:
            self.fail('empty_name')
        return data


class ListSKUSerializer(SKUSerializer):
    category = IdNameCharSerializer(source='category')
    brand = IdNameCharSerializer()
    country = IdNameSerializer(many=True)

    class Meta(SKUSerializer.Meta):
        fields = (
            'id',
            'name',
            'category',
            'brand',
            'country'
        )


class UpdateSKUSerializer(SKUSerializer):
    class Meta(SKUSerializer.Meta):
        fields = (
            'name',
            'brand',
            'category',
            'country'
        )


class ImportSKUSerializer(CSVFileInputSerializer):
    pass
