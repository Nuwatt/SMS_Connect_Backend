from rest_framework import serializers

from apps.market.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class AddStoreSerializer(StoreSerializer):
    class Meta(StoreSerializer.Meta):
        fields = (
            'name',
            'retailer',
        )


class ListStoreSerializer(StoreSerializer):
    class Meta(StoreSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class UpdateStoreSerializer(AddStoreSerializer):
    pass
