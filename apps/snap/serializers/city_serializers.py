from rest_framework import serializers

from apps.snap.models import SnapCity


class SnapCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapCity
        fields = '__all__'


class AddSnapSnapCitySerializer(SnapCitySerializer):
    class Meta(SnapCitySerializer.Meta):
        fields = (
            'name',
            'country'
        )


class ListSnapSnapCitySerializer(SnapCitySerializer):
    class Meta(SnapCitySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateSnapCitySerializer(AddSnapSnapCitySerializer):
    pass
