from rest_framework import serializers


class SKUMinMaxReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    max = serializers.FloatField(default=0)
    min = serializers.FloatField(default=0)
    mode = serializers.FloatField(default=0)
    mean = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class BrandMinMaxReportSerializer(serializers.Serializer):
    brand = serializers.CharField(source='name')
    max = serializers.FloatField(default=0)
    min = serializers.FloatField(default=0)
    mode = serializers.FloatField(default=0)
    mean = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class SKUMonthReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    month = serializers.DateTimeField(format='%b')
    value = serializers.FloatField()


class CountryReportSerializer(serializers.Serializer):
    country = serializers.CharField()
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class CityReportSerializer(serializers.Serializer):
    city = serializers.CharField()
    value = serializers.DecimalField(default=0, decimal_places=2, max_digits=10)


class SKUCountryReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    country = serializers.CharField()
    value = serializers.FloatField()


class AnswerReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()


class AnswerPerCountryReportSerializer(serializers.Serializer):
    country = serializers.CharField(source='name')
    value = serializers.FloatField()


class AnswerPerCityReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='name')
    value = serializers.FloatField()


class TotalVisitReportSerializer(serializers.Serializer):
    city = serializers.CharField(source='name')
    value = serializers.IntegerField()
