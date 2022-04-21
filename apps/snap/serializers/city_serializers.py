from rest_framework import serializers

from apps.snap.models import SnapCity


class SnapCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapCity
        fields = '__all__'


class AddSnapCitySerializer(SnapCitySerializer):
    class Meta(SnapCitySerializer.Meta):
        fields = (
            'name',
            'country'
        )


class ListSnapCitySerializer(SnapCitySerializer):
    country_id = serializers.IntegerField()

    class Meta(SnapCitySerializer.Meta):
        fields = (
            'id',
            'name',
            'country_id'
        )


class UpdateSnapCitySerializer(AddSnapCitySerializer):
    pass
