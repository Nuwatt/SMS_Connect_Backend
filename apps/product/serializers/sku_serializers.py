from rest_framework import serializers

from apps.core.serializers import IdNameSerializer, CSVFileInputSerializer
from apps.product.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'


class AddSKUSerializer(SKUSerializer):
    names = serializers.ListSerializer(child=serializers.CharField())

    class Meta(SKUSerializer.Meta):
        fields = (
            'names',
            'category',
            'brand'
        )


class ListSKUSerializer(SKUSerializer):
    category = IdNameSerializer()
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
            'category',
            'brand'
        )


class ImportSKUSerializer(CSVFileInputSerializer):
    pass
