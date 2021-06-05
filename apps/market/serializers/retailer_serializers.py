from rest_framework import serializers

from apps.core.serializers import IdNameSerializer, CSVFileInputSerializer
from apps.market.models import Retailer


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'


class AddRetailerSerializer(RetailerSerializer):
    name = serializers.ListSerializer(child=serializers.CharField())

    class Meta(RetailerSerializer.Meta):
        fields = (
            'name',
            'channel',
        )


class ListRetailerSerializer(RetailerSerializer):
    channel = IdNameSerializer()

    class Meta(RetailerSerializer.Meta):
        fields = (
            'id',
            'name',
            'channel',
        )


class UpdateRetailerSerializer(RetailerSerializer):
    class Meta(RetailerSerializer.Meta):
        fields = (
            'name',
            'channel',
        )


class ImportRetailerSerializer(CSVFileInputSerializer):
    pass
