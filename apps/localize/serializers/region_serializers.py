from rest_framework import serializers

from apps.localize.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class AddRegionSerializer(RegionSerializer):
    class Meta(RegionSerializer.Meta):
        fields = (
            'name',
        )


class ListRegionSerializer(RegionSerializer):
    class Meta(RegionSerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateRegionSerializer(AddRegionSerializer):
    pass
