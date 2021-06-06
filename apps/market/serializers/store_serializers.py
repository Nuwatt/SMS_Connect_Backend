from django.db.models import fields
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.market.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class AddStoreRetailerSerializer(StoreSerializer):
    # for adding store and retailer
    name = serializers.ListSerializer(child=serializers.CharField())
    retailer = serializers.ListSerializer(child=serializers.CharField())

    class meta(StoreSerializer.Meta):
        fields = (
            'name',
            'channel',
            'retailer',
            'city'
        )
    
    default_error_messages = {
        'empty_name': _('Requires in list.'),
        'empty_retailer': _('Retailer name is required')

    }

    def validate_name(self, data):
        if len(data.name) == 0:
            self.fail('empty_name')
        if len(data.retailer) == 0:
            self.fail('empty_retailer')
        return data
    

class AddStoreSerializer(StoreSerializer):
    name = serializers.ListSerializer(child=serializers.CharField())

    class Meta(StoreSerializer.Meta):
        fields = (
            'name',
            'retailer',
            'city',
        )

    default_error_messages = {
        'empty_name': _('Requires in list.')
    }

    def validate_name(self, data):
        if len(data) == 0:
            self.fail('empty_name')
        return data


class ListStoreSerializer(StoreSerializer):
    retailer = IdNameSerializer()
    city = IdNameSerializer()

    class Meta(StoreSerializer.Meta):
        fields = (
            'id',
            'retailer',
            'name',
            'city',
        )


class ListStoreForAgentUserSerializer(StoreSerializer):
    retailer = IdNameSerializer()

    class Meta(StoreSerializer.Meta):
        fields = (
            'id',
            'retailer',
            'name',
        )


class UpdateStoreSerializer(StoreSerializer):
    class Meta(StoreSerializer.Meta):
        fields = (
            'name',
            'retailer',
        )
