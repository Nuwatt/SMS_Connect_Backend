from rest_framework import serializers


class SKUOverallReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    available = serializers.FloatField(default=0)
    not_available = serializers.FloatField(default=0)
    less = serializers.FloatField(default=0)


class SKUCityReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    city = serializers.CharField()
    value = serializers.FloatField()


class SKUStoreReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    store = serializers.CharField()
    value = serializers.FloatField()


class SKURetailerReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    retailer = serializers.CharField()
    value = serializers.FloatField()