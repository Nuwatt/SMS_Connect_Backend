from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.localize.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AddCitySerializer(CitySerializer):
    class Meta(CitySerializer.Meta):
        fields = (
            'name',
            'country'
        )


class ListCitySerializer(CitySerializer):
    country = IdNameSerializer()

    class Meta(CitySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateCitySerializer(AddCitySerializer):
    pass
