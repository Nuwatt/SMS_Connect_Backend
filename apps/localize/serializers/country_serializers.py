from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.localize.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AddCountrySerializer(CountrySerializer):
    class Meta(CountrySerializer.Meta):
        fields = (
            'name', 
            'region'
        )


class ListCountrySerializer(CountrySerializer):
    city = IdNameSerializer(many=True, source='city_set')

    class Meta(CountrySerializer.Meta):
        fields = (
            'id',
            'name',
            'city'
        )


class ListNationalitySerializer(CountrySerializer):
    class Meta(CountrySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateCountrySerializer(AddCountrySerializer):
    pass
