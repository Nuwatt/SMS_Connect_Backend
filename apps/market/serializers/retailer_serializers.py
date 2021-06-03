from rest_framework import serializers

from apps.core.serializers import IdNameSerializer, CSVFileInputSerializer
from apps.market.models import Retailer


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'


class AddRetailerSerializer(RetailerSerializer):
    class Meta(RetailerSerializer.Meta):
        fields = (
            'name',
            'channel',
        )


class ListRetailerSerializer(AddRetailerSerializer):
    channel = IdNameSerializer()

    class Meta(AddRetailerSerializer.Meta):
        fields = (
                     'id',
                 ) + AddRetailerSerializer.Meta.fields


class UpdateRetailerSerializer(AddRetailerSerializer):
    pass


class ImportRetailerSerializer(CSVFileInputSerializer):
    pass
