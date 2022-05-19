from rest_framework import serializers


class CityPriceMonitorSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    city = serializers.CharField(source='city_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)


class ChannelPriceMonitorSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)


class BrandPriceMonitorSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    brand = serializers.CharField(source='brand_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)


class ChannelCityPriceMonitorSnapReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='city_name')
    month = serializers.DateField(format='%b\'%-y')
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)
