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


class OverviewOutOfStockSnapReport(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    available = serializers.FloatField()
    not_available = serializers.FloatField()
    less = serializers.FloatField()


class OutOfStockSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b')
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField()


class ByCityOutOfStockSnapReportSerializer(serializers.Serializer):
    city = serializers.DateField(source='city_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField()


class VisitByCityOutOfStockSnapReportSerializer(serializers.Serializer):
    city = serializers.DateField(source='city_name')
    value = serializers.FloatField()


class NotAvailableByWeekOutOfStockSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    week = serializers.IntegerField()
    retailer = serializers.CharField(source='retailer_name')
    store = serializers.CharField(source='store_name')


class BulkDeleteOutOfStockSnapSerializer(serializers.Serializer):
    snap_ids = serializers.ListSerializer(child=serializers.IntegerField())
