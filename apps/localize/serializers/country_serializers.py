from drf_yasg.utils import swagger_serializer_method
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
    city = serializers.SerializerMethodField()

    class Meta(CountrySerializer.Meta):
        fields = (
            'id',
            'name',
            'city'
        )

    @swagger_serializer_method(serializer_or_field=IdNameSerializer())
    def get_city(self, instance):
        query_params = self.context['request'].query_params
        if query_params.get('questionnaire', None):
            city = instance.city_set.filter(questionnaire__id=query_params.get('questionnaire'))
        else:
            city = instance.city_set.all()
        return IdNameSerializer(city, many=True).data


class ListNationalitySerializer(CountrySerializer):
    class Meta(CountrySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateCountrySerializer(AddCountrySerializer):
    pass
