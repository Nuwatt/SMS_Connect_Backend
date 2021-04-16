from rest_framework import serializers

from apps.product.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class AddBrandSerializer(BrandSerializer):
    class Meta(BrandSerializer.Meta):
        fields = (
            'name',
        )


class ListBrandSerializer(BrandSerializer):
    class Meta(BrandSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateBrandSerializer(AddBrandSerializer):
    pass
