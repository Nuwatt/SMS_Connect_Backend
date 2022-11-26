from rest_framework import serializers

from apps.core.serializers import (
    CSVFileInputSerializer
)
from apps.report.serializers.distribution_check_serializers import (
    VisitPerCountryReportSerializer,
    VisitPerCityReportSerializer,
    VisitPerChannelReportSerializer,
    SKUPerCityReportSerializer
)
from apps.snap.models import SnapDistribution


class ImportDistributionSnapSerializer(CSVFileInputSerializer):
    pass


class DistributionSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnapDistribution
        fields = '__all__'


class ListDistributionSnapSerializer(DistributionSnapSerializer):
    country = serializers.CharField(source='country_name')
    city = serializers.CharField(source='city_name')
    category = serializers.CharField(source='category_name')
    brand = serializers.CharField(source='brand_name')
    channel = serializers.CharField(source='channel_name')
    sku = serializers.CharField(source='sku_name')

    class Meta(DistributionSnapSerializer.Meta):
        fields = (
            'id',
            'date',
            'country',
            'city',
            'channel',
            'category',
            'brand',
            'sku',
            'total_distribution',
            'shelf_share',
            'number_of_outlet'
        )


class UpdateDistributionSnapSerializer(DistributionSnapSerializer):
    class Meta(DistributionSnapSerializer.Meta):
        fields = (
            'total_distribution',
        )


class VisitByCountryDistributionSnapReport(VisitPerCountryReportSerializer):
    pass


class VisitByCityDistributionSnapReportSerializer(VisitPerCityReportSerializer):
    pass


class VisitByChannelDistributionSnapReportSerializer(VisitPerChannelReportSerializer):
    pass


class SKUByCityDistributionSnapReportSerializer(SKUPerCityReportSerializer):
    pass


class TotalDistributionSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=0)


class ShelfShareDistributionSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    city = serializers.CharField(source='city_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=0)


class NumberOfOutletDistributionSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    value = serializers.DecimalField(max_digits=10, decimal_places=0)


class BulkDeleteDistributionSnapSerializer(serializers.Serializer):
    snap_ids = serializers.ListSerializer(child=serializers.IntegerField())


class ListDistributionSnapMonthSerializer(serializers.Serializer):
    name = serializers.DateField(format='%b\'%-y', source='month')
    id = serializers.DateField(format='%Y-%m-%d', source='month')
