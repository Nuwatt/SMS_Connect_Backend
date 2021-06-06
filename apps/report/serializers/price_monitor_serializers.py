from rest_framework import serializers


class SKUMinMaxReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    max = serializers.FloatField(default=0)
    min = serializers.FloatField(default=0)
    mode = serializers.FloatField(default=0)
    mean = serializers.FloatField(default=0)


class SKUMonthReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    month = serializers.DateTimeField(format='%b')
    value = serializers.FloatField()


class CountryReportSerializer(serializers.Serializer):
    country = serializers.CharField()
    value = serializers.FloatField()


class CityReportSerializer(serializers.Serializer):
    city = serializers.CharField()
    value = serializers.FloatField()


class SKUCountryReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    country = serializers.CharField()
    value = serializers.FloatField()


class AnswerReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()


class AnswerPerCountryReportSerializer(SKUCountryReportSerializer):
    pass
    # sku = serializers.CharField()
    # statistics = CountryReportSerializer(many=True)


class AnswerPerCityReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='name')
    city = serializers.CharField()
    value = serializers.FloatField()


class TotalVisitReportSerializer(serializers.Serializer):
    sku = serializers.CharField(source='sku_name')
    city = serializers.CharField(source='name')
    value = serializers.IntegerField()
