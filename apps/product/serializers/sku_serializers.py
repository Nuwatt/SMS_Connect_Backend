from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.serializers import IdNameSerializer, CSVFileInputSerializer
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
            'brand'
        )

    def validate_name(self, data):
        if len(data) == 0:
            self.fail('empty_name')
        return data


class ListSKUSerializer(SKUSerializer):
    category = IdNameSerializer(source='brand.category')
    brand = IdNameSerializer()

    class Meta(SKUSerializer.Meta):
        fields = (
            'id',
            'name',
            'category',
            'brand'
        )


class UpdateSKUSerializer(SKUSerializer):
    class Meta(SKUSerializer.Meta):
        fields = (
            'name',
            'brand'
        )


class ImportSKUSerializer(CSVFileInputSerializer):
    pass
