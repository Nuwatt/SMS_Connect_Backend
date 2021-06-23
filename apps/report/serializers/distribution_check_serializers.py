from rest_framework import serializers


class VisitPerCountryReportSerializer(serializers.Serializer):
    country = serializers.CharField(source='country_name')
    value = serializers.FloatField()


class VisitPerCityReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='city_name')
    value = serializers.FloatField()


class VisitPerChannelReportSerializer(serializers.Serializer):
    channel = serializers.CharField(source='channel_name')
    value = serializers.FloatField()


class SKUPerCityReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    city = serializers.CharField(source='city_name')
    value = serializers.FloatField()
