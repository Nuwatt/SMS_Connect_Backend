from rest_framework import serializers


class SKUMinMaxReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    max = serializers.FloatField(default=0)
    min = serializers.FloatField(default=0)
    mode = serializers.FloatField(default=0)
    mean = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class BrandMinMaxReportSerializer(serializers.Serializer):
    brand = serializers.CharField(source='brand_name')
    max = serializers.FloatField(default=0)
    min = serializers.FloatField(default=0)
    mode = serializers.FloatField(default=0)
    mean = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class SKUMonthReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    month = serializers.DateTimeField(format='%b')
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class CountryReportSerializer(serializers.Serializer):
    country = serializers.CharField()
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class CityReportSerializer(serializers.Serializer):
    city = serializers.CharField()
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class SKUCountryReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    country = serializers.CharField(source='country_name')
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class AnswerReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()


class AnswerPerSKUReportSerializer(serializers.Serializer):
    name = serializers.CharField(source='sku_name')
    value = serializers.IntegerField()


class AnswerPerCountryReportSerializer(serializers.Serializer):
    country = serializers.CharField(source='country_name')
    value = serializers.FloatField()


class AnswerPerCityReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='city_name')
    value = serializers.FloatField()


class TotalVisitReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='name')
    value = serializers.IntegerField()
