from rest_framework import serializers

from apps.localize.models import Nationality


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'


class AddNationalitySerializer(NationalitySerializer):
    class Meta(NationalitySerializer.Meta):
        fields = (
            'name',
        )


class ListNationalitySerializer(NationalitySerializer):
    class Meta(NationalitySerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateNationalitySerializer(AddNationalitySerializer):
    pass
