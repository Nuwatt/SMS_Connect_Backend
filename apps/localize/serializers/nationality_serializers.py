from rest_framework import serializers

from apps.localize.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class AddNationalitySerializer(CountrySerializer):
    class Meta(CountrySerializer.Meta):
        fields = (
            'name',
        )


class ListNationalitySerializer(CountrySerializer):
    class Meta(CountrySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateNationalitySerializer(AddNationalitySerializer):
    pass
