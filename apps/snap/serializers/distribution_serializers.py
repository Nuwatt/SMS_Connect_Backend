from rest_framework import serializers

from apps.core.serializers import (
    CSVFileInputSerializer,
    IdNameSerializer,
    IdNameCharSerializer
)
from apps.report.serializers.distribution_check_serializers import (
    VisitPerCountryReportSerializer,
    VisitPerCityReportSerializer,
    VisitPerChannelReportSerializer,
    SKUPerCityReportSerializer,
    SKUPerCountryReportSerializer,
    SKUPerChannelReportSerializer
)
from apps.report.serializers.price_monitor_serializers import (
    AnswerPerCountryReportSerializer,
    AnswerPerCityReportSerializer
)
from apps.snap.models import DistributionSnap


class ImportDistributionSnapSerializer(CSVFileInputSerializer):
    pass


class DistributionSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionSnap
        fields = '__all__'


class ListDistributionSnapSerializer(DistributionSnapSerializer):
    country = IdNameSerializer(source='city.country')
    city = IdNameSerializer()
    category = IdNameCharSerializer(source='sku.category')
    brand = IdNameCharSerializer(source='sku.brand')
    channel = IdNameSerializer()
    sku = IdNameCharSerializer()

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
    value = serializers.FloatField(source='total_distribution')


class ShelfShareDistributionSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField(source='shelf_share')


class NumberOfOutletDistributionSnapReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    value = serializers.FloatField(source='number_of_outlet')


class BulkDeleteDistributionSnapSerializer(serializers.Serializer):
    snap_ids = serializers.ListSerializer(child=serializers.IntegerField())
