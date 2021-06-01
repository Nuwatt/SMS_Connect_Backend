from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.market.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class AddStoreSerializer(StoreSerializer):
    names = serializers.ListSerializer(child=serializers.CharField())

    class Meta(StoreSerializer.Meta):
        fields = (
            'names',
            'retailer',
        )


class ListStoreSerializer(StoreSerializer):
    retailer = IdNameSerializer()

    class Meta(StoreSerializer.Meta):
        fields = (
            'id',
            'retailer',
            'name',
        )


class UpdateStoreSerializer(AddStoreSerializer):
    pass
