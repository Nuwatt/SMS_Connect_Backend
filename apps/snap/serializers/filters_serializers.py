from rest_framework import serializers


class ListSKUFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='sku_id')
    name = serializers.CharField(source='sku_name')


class ListBrandFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='brand_id')
    name = serializers.CharField(source='brand_name')


class ListCategoryFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='category_id')
    name = serializers.CharField(source='category_name')


class ListRetailerFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='retailer_id')
    name = serializers.CharField(source='retailer_name')


class ListStoreFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='retailer_id')
    name = serializers.CharField(source='retailer_name')


class ListCityFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='city_id')
    name = serializers.CharField(source='city_name')


class ListCountryFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='country_id')
    name = serializers.CharField(source='country_name')


class ListChannelFiltersSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='channel_id')
    name = serializers.CharField(source='channel_name')
