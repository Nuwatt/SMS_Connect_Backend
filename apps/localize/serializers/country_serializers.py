from rest_framework import serializers

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
    class Meta(CountrySerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateCountrySerializer(AddCountrySerializer):
    pass
