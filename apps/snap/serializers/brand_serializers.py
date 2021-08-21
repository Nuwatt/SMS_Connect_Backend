from rest_framework import serializers

from apps.snap.models import SnapBrand


class SnapBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapBrand
        fields = '__all__'


class AddSnapBrandSerializer(SnapBrandSerializer):
    class Meta(SnapBrandSerializer.Meta):
        fields = (
            'name',
        )


class ListSnapBrandSerializer(AddSnapBrandSerializer):
    class Meta(AddSnapBrandSerializer.Meta):
        fields = (
            'id',
        ) + AddSnapBrandSerializer.Meta.fields


class UpdateSnapBrandSerializer(AddSnapBrandSerializer):
    pass
