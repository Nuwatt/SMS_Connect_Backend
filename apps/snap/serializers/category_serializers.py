from rest_framework import serializers

from apps.snap.models import SnapCategory


class SnapCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapCategory
        fields = '__all__'


class AddSnapCategorySerializer(SnapCategorySerializer):
    class Meta(SnapCategorySerializer.Meta):
        fields = (
            'name',
        )


class ListSnapCategorySerializer(SnapCategorySerializer):
    class Meta(SnapCategorySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateSnapCategorySerializer(AddSnapCategorySerializer):
    pass
