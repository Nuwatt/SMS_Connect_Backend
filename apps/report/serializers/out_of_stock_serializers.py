from rest_framework import serializers


class SKUOverallReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    available = serializers.FloatField(default=0)
    not_available = serializers.FloatField(default=0)
    less = serializers.FloatField(default=0)


class SKUCityReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    city = serializers.CharField(source='city_name')
    value = serializers.FloatField()


class SKUStoreReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    store = serializers.CharField(source='store_name')
    value = serializers.FloatField()


class SKUWeekNotAvailableReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    week = serializers.IntegerField()
    retailer = serializers.CharField(source='store__retailer__name')
    store = serializers.CharField(source='store__name')
