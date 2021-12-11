from datetime import timedelta

from rest_framework import serializers

from apps.report.serializers.price_monitor_serializers import SKUMonthReportSerializer


class SKUOverallReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    available = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)
    not_available = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)
    less = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class SKUCityReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    city = serializers.CharField(source='city_name')
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class SKUStoreReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    store = serializers.CharField(source='store_name')
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class SKUWeekNotAvailableReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    week = serializers.SerializerMethodField()
    retailer = serializers.CharField(source='retailer_name')
    store = serializers.CharField(source='store_name')

    def get_week(self, instance):
        start_date = instance.get('completed_week')
        end_date = start_date + timedelta(days=6)
        return f'{start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}'


class SKUMonthAvailableReportSerializer(SKUMonthReportSerializer):
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)


class SKUMonthNotAvailableReportSerializer(SKUMonthReportSerializer):
    value = serializers.DecimalField(default=0, decimal_places=1, max_digits=4)
