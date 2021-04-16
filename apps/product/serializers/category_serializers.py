from rest_framework import serializers

from apps.product.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AddCategorySerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = (
            'name',
        )


class ListCategorySerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateCategorySerializer(AddCategorySerializer):
    pass
