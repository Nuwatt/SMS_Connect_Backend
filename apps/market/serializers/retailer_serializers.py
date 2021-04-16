from rest_framework import serializers

from apps.market.models import Retailer


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'


class AddRetailerSerializer(RetailerSerializer):
    class Meta(RetailerSerializer.Meta):
        fields = (
            'name',
        )


class ListRetailerSerializer(RetailerSerializer):
    class Meta(RetailerSerializer.Meta):
        fields = (
            'id',
            'name'
        )


class UpdateRetailerSerializer(AddRetailerSerializer):
    pass
