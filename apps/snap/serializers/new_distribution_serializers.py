from rest_framework import serializers


class DistributionSnapReportSerializer(serializers.Serializer):
    month = serializers.DateField(format='%b\'%-y')
    sku = serializers.CharField(source='sku_name')
    total_distribution = serializers.DecimalField(
        source='total_distribution_value',
        max_digits=10,
        decimal_places=1
    )
    shelf_share = serializers.DecimalField(
        source='shelf_share_value',
        max_digits=10,
        decimal_places=1
    )


class DistributionSnapCityReportSerializer(DistributionSnapReportSerializer):
    city = serializers.CharField(source='city_name')


class DistributionSnapCountryReportSerializer(DistributionSnapReportSerializer):
    country = serializers.CharField(source='country_name')


class DistributionSnapBrandReportSerializer(DistributionSnapReportSerializer):
    brand = serializers.CharField(source='brand_name')


class DistributionSnapChannelReportSerializer(DistributionSnapReportSerializer):
    channel = serializers.CharField(source='channel_name')


class DistributionSnapSKUReportSerializer(DistributionSnapReportSerializer):
    pass
