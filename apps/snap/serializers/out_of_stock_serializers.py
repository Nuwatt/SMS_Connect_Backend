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
    country = serializers.CharField(source='city__country__name')
    city = serializers.CharField(source='city__name')
    category = serializers.CharField(source='sku__category__name')
    brand = serializers.CharField(source='sku__brand__name')
    channel = serializers.CharField(source='store__channel__name')
    store = serializers.CharField(source='store__name')
    retailer = serializers.CharField(source='store__retailer__name')
    sku = serializers.CharField(source='sku__name')

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
    available = serializers.DecimalField(max_digits=4, decimal_places=1)
    not_available = serializers.DecimalField(max_digits=4, decimal_places=1)
    less = serializers.DecimalField(max_digits=4, decimal_places=1)


class OutOfStockSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=4, decimal_places=1)


class ByCityOutOfStockSnapReportSerializer(serializers.Serializer):
    city = serializers.DateField(source='city_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=4, decimal_places=1)


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
