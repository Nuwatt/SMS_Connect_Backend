from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.product.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class AddBrandSerializer(BrandSerializer):
    class Meta(BrandSerializer.Meta):
        fields = (
            'name',
            'category',
        )


class ListBrandSerializer(AddBrandSerializer):
    category = IdNameSerializer()

    class Meta(AddBrandSerializer.Meta):
        fields = (
            'id',
        ) + AddBrandSerializer.Meta.fields


class UpdateBrandSerializer(AddBrandSerializer):
    pass
