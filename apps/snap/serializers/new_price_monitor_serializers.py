from rest_framework import serializers


class CityMaxPriceMonitorSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    city = serializers.CharField(source='city_name')
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=1)
