from rest_framework import serializers

from apps.snap.models import SnapCountry


class SnapCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapCountry
        fields = '__all__'


class AddSnapCountrySerializer(SnapCountrySerializer):
    class Meta(SnapCountrySerializer.Meta):
        fields = (
            'name',
        )


class ListSnapCountrySerializer(SnapCountrySerializer):
    class Meta(SnapCountrySerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateSnapCountrySerializer(AddSnapCountrySerializer):
    pass
