from rest_framework import serializers

from apps.localize.models import Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class AddAreaSerializer(AreaSerializer):
    class Meta(AreaSerializer.Meta):
        fields = (
            'name',
            'city'
        )


class ListAreaSerializer(AddAreaSerializer):
    class Meta(AddAreaSerializer.Meta):
        fields = (
            'id',
        ) + AddAreaSerializer.Meta.fields


class UpdateAreaSerializer(AddAreaSerializer):
    pass
