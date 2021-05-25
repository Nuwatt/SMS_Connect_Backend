from rest_framework import serializers

from apps.core.serializers import IdNameSerializer, CSVFileInputSerializer
from apps.product.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'


class AddSKUSerializer(SKUSerializer):
    class Meta(SKUSerializer.Meta):
        fields = (
            'name',
            'category',
            'brand'
        )


class ListSKUSerializer(AddSKUSerializer):
    category = IdNameSerializer()
    brand = IdNameSerializer()

    class Meta(AddSKUSerializer.Meta):
        fields = (
                     'id',
                 ) + AddSKUSerializer.Meta.fields


class UpdateSKUSerializer(AddSKUSerializer):
    pass


class ImportSKUSerializer(CSVFileInputSerializer):
    pass
