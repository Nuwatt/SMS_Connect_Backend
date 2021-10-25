from rest_framework import serializers

from apps.core.serializers import (
    CSVFileInputSerializer,
    IdNameSerializer,
    IdNameCharSerializer
)
from apps.report.serializers.price_monitor_serializers import (
    AnswerPerCountryReportSerializer,
    AnswerPerCityReportSerializer
)
from apps.snap.models import PriceMonitorSnap


class ImportPriceMonitorSnapSerializer(CSVFileInputSerializer):
    pass


class PriceMonitorSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceMonitorSnap
        fields = '__all__'


class ListPriceMonitorSnapSerializer(PriceMonitorSnapSerializer):
    country = serializers.CharField(source='city__country__name')
    city = serializers.CharField(source='city__name')
    category = serializers.CharField(source='sku__category__name')
    brand = serializers.CharField(source='sku__brand__name')
    channel = serializers.CharField(source='channel__name')
    sku = serializers.CharField(source='sku__name')

    class Meta(PriceMonitorSnapSerializer.Meta):
        fields = (
            'id',
            'date',
            'country',
            'city',
            'channel',
            'category',
            'brand',
            'sku',
            'count',
            'min',
            'min',
            'max',
            'mean',
            'mode'
        )


class UpdatePriceMonitorSnapSerializer(PriceMonitorSnapSerializer):
    class Meta(PriceMonitorSnapSerializer.Meta):
        fields = (
            'count',
            'min',
            'min',
            'max',
            'mean',
            'mode'
        )


class OverviewPriceMonitorSnapReport(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    min = serializers.DecimalField(max_digits=10, decimal_places=1, source='min_value')
    max = serializers.DecimalField(max_digits=10, decimal_places=1, source='max_value')
    mode = serializers.DecimalField(max_digits=10, decimal_places=1, source='mode_value')
    mean = serializers.DecimalField(max_digits=10, decimal_places=1, source='mean_value')


class MonthPriceMonitorSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)


class BrandoverviewPriceMonitorSnapReportSerializer(serializers.Serializer):
    brand = serializers.CharField(source='brand_name')
    min = serializers.DecimalField(max_digits=10, decimal_places=1, source='min_value')
    max = serializers.DecimalField(max_digits=10, decimal_places=1, source='max_value')
    mode = serializers.DecimalField(max_digits=10, decimal_places=1, source='mode_value')
    mean = serializers.DecimalField(max_digits=10, decimal_places=1, source='mean_value')


class CountryPriceMonitorSnapReportSerializer(serializers.Serializer):
    country = serializers.CharField(source='country_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)


class VisitPerCityPriceMonitorSnapReportSerializer(AnswerPerCityReportSerializer):
    pass


class VisitPerCountryPriceMonitorSnapReportSerializer(AnswerPerCountryReportSerializer):
    pass


class SKUPerChannelPriceMonitorSnapReportSerializer(serializers.Serializer):
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)


class BulkDeletePriceMonitorSnapSerializer(serializers.Serializer):
    snap_ids = serializers.ListSerializer(child=serializers.IntegerField())
