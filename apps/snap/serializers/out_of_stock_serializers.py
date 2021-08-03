from rest_framework import serializers

from apps.core.serializers import CSVFileInputSerializer, IdNameSerializer, IdNameCharSerializer
from apps.report.serializers.price_monitor_serializers import AnswerPerCountryReportSerializer, \
    AnswerPerCityReportSerializer
from apps.snap.models import PriceMonitorSnap, OutOfStockSnap


class ImportOutOfStockSnapSerializer(CSVFileInputSerializer):
    pass


class OutOfStockSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfStockSnap
        fields = '__all__'


class ListOutOfStockSnapSerializer(OutOfStockSnapSerializer):
    country = IdNameSerializer(source='city.country')
    city = IdNameSerializer()
    category = IdNameCharSerializer(source='sku.category')
    brand = IdNameCharSerializer(source='sku.brand')
    channel = IdNameSerializer(source='store.channel')
    store = IdNameSerializer()
    retailer = IdNameSerializer(source='store.retailer')
    sku = IdNameCharSerializer()

    class Meta(OutOfStockSnapSerializer.Meta):
        fields = (
            'id',
            'date',
            'country',
            'city',
            'channel',
            'retailer',
            'store',
            'category',
            'brand',
            'sku',
            'count',
            'not_available_in_month',
            'less_available_in_month',
            'available_in_month',
            'not_available_by_store',
            'less_available_by_store',
            'available_by_store',
            'not_available_by_city',
            'less_available_by_city',
            'available_by_city',
        )


class UpdateOutOfStockSnapSerializer(OutOfStockSnapSerializer):
    class Meta(OutOfStockSnapSerializer.Meta):
        fields = (
            'count',
            'not_available_in_month',
            'less_available_in_month',
            'available_in_month',
            'not_available_by_store',
            'less_available_by_store',
            'available_by_store',
            'not_available_by_city',
            'less_available_by_city',
            'available_by_city',
        )


class OverviewPriceMonitorSnapReport(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    min = serializers.FloatField(source='min_value')
    max = serializers.FloatField(source='max_value')
    mode = serializers.FloatField(source='mode_value')
    mean = serializers.DecimalField(max_digits=10, decimal_places=1, source='mean_value')


class MonthPriceMonitorSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b')
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField()


class BrandoverviewPriceMonitorSnapReportSerializer(serializers.Serializer):
    brand = serializers.CharField(source='brand_name')
    min = serializers.FloatField(source='min_value')
    max = serializers.FloatField(source='max_value')
    mode = serializers.FloatField(source='mode_value')
    mean = serializers.DecimalField(max_digits=10, decimal_places=1, source='mean_value')


class CountryPriceMonitorSnapReportSerializer(serializers.Serializer):
    country = serializers.CharField(source='country_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField()


class VisitPerCityPriceMonitorSnapReportSerializer(AnswerPerCityReportSerializer):
    pass


class VisitPerCountryPriceMonitorSnapReportSerializer(AnswerPerCountryReportSerializer):
    pass


class SKUPerChannelPriceMonitorSnapReportSerializer(serializers.Serializer):
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField()
