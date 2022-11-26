from rest_framework import serializers

from apps.core.serializers import (
    CSVFileInputSerializer
)
from apps.snap.models import SnapOutOfStock


class ImportOutOfStockSnapSerializer(CSVFileInputSerializer):
    pass


class OutOfStockSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapOutOfStock
        fields = '__all__'


class ListOutOfStockSnapSerializer(OutOfStockSnapSerializer):
    country = serializers.CharField(source='country_name')
    city = serializers.CharField(source='city_name')
    category = serializers.CharField(source='category_name')
    brand = serializers.CharField(source='brand_name')
    channel = serializers.CharField(source='channel_name')
    store = serializers.CharField(source='store_name')
    retailer = serializers.CharField(source='retailer_name')
    sku = serializers.CharField(source='sku_name')

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
    available = serializers.DecimalField(max_digits=3, decimal_places=0)
    not_available = serializers.DecimalField(max_digits=3, decimal_places=0)
    less = serializers.DecimalField(max_digits=3, decimal_places=0)


class OutOfStockSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=3, decimal_places=0)


class ByCityOutOfStockSnapReportSerializer(serializers.Serializer):
    city = serializers.DateField(source='city_name')
    month = serializers.DateField(format='%b\'%-y')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=3, decimal_places=0)


class VisitByCityOutOfStockSnapReportSerializer(serializers.Serializer):
    city = serializers.DateField(source='city_name')
    value = serializers.FloatField()


class NotAvailableByWeekOutOfStockSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    week = serializers.DateField()
    retailer = serializers.CharField(source='retailer_name')
    store = serializers.CharField(source='store_name')


class BulkDeleteOutOfStockSnapSerializer(serializers.Serializer):
    snap_ids = serializers.ListSerializer(child=serializers.IntegerField())


class OutOfStockSnapCityReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='city_name')
    month = serializers.DateField(format='%b\'%-y')
    sku = serializers.CharField(source='sku_name')
    not_available_by_city = serializers.DecimalField(
        source='not_available_by_city_value',
        max_digits=3,
        decimal_places=0
    )
    less_available_by_city = serializers.DecimalField(
        source='less_available_by_city_value',
        max_digits=3,
        decimal_places=0
    )
    available_by_city = serializers.DecimalField(
        source='available_by_city_value',
        max_digits=3,
        decimal_places=0
    )


class OutOfStockSnapCityChannelReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    city = serializers.CharField(source='city_name')
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')
    not_available_by_city = serializers.DecimalField(
        source='not_available_by_city_value',
        max_digits=3,
        decimal_places=0
    )
    less_available_by_city = serializers.DecimalField(
        source='less_available_by_city_value',
        max_digits=3,
        decimal_places=0
    )
    available_by_city = serializers.DecimalField(
        source='available_by_city_value',
        max_digits=3,
        decimal_places=0
    )


class OutOfStockSnapStoreStoreReportSerializer(serializers.Serializer):
    store = serializers.CharField(source='store_name')
    month = serializers.DateField(format='%b\'%-y')
    sku = serializers.CharField(source='sku_name')
    not_available_by_store = serializers.DecimalField(
        source='not_available_by_store_value',
        max_digits=3,
        decimal_places=0
    )
    less_available_by_store = serializers.DecimalField(
        source='less_available_by_store_value',
        max_digits=3,
        decimal_places=0
    )
    available_by_store = serializers.DecimalField(
        source='available_by_store_value',
        max_digits=3,
        decimal_places=0
    )


class OutOfStockSnapStoreMonthReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    sku = serializers.CharField(source='sku_name')
    not_available_by_month = serializers.DecimalField(
        source='not_available_by_month_value',
        max_digits=3,
        decimal_places=0
    )
    less_available_by_month = serializers.DecimalField(
        source='less_available_by_month_value',
        max_digits=3,
        decimal_places=0
    )
    available_by_month = serializers.DecimalField(
        source='available_by_month_value',
        max_digits=3,
        decimal_places=0
    )


class ListOutOfStockSnapMonthSerializer(serializers.Serializer):
    name = serializers.DateField(format='%b\'%-y', source='month')
    id = serializers.DateField(format='%Y-%m-%d', source='month')
