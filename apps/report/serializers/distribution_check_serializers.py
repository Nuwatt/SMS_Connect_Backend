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


class SKUPerCityReportSerializer(VisitPerCityReportSerializer):
    sku = serializers.CharField(source='sku_name')


class SKUPerCountryReportSerializer(VisitPerCountryReportSerializer):
    sku = serializers.CharField(source='sku_name')


class SKUPerChannelReportSerializer(VisitPerChannelReportSerializer):
    sku = serializers.CharField(source='sku_name')


class BrandPerCityReportSerializer(VisitPerCityReportSerializer):
    brand = serializers.CharField(source='brand_name')


class BrandPerCountryReportSerializer(VisitPerCountryReportSerializer):
    brand = serializers.CharField(source='brand_name')


class BrandPerChannelReportSerializer(VisitPerChannelReportSerializer):
    brand = serializers.CharField(source='brand_name')


class AvgPerSKUReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class AvgPerBrandReportSerializer(serializers.Serializer):
    brand = serializers.CharField(source='brand_name')
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class AvgSKUPerChannelReportSerializer(serializers.Serializer):
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class AvgBrandPerChannelReportSerializer(serializers.Serializer):
    channel = serializers.CharField(source='channel_name')
    brand = serializers.CharField(source='brand_name')
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)
