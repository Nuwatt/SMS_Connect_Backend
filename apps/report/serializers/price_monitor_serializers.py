from rest_framework import serializers


class SKUMinMaxReportSerializer(serializers.Serializer):
    sku = serializers.CharField()
    max = serializers.FloatField()
    min = serializers.FloatField()
    mode = serializers.FloatField()
    mean = serializers.FloatField()


class MonthReportSerializer(serializers.Serializer):
    month = serializers.DateTimeField(source='date_time', format='%B')
    value = serializers.FloatField()


class SKUMonthReportSerializer(serializers.Serializer):
    sku = serializers.CharField()
    statistics = MonthReportSerializer(many=True)


class CountryReportSerializer(serializers.Serializer):
    country = serializers.CharField()
    value = serializers.FloatField()


class CityReportSerializer(serializers.Serializer):
    city = serializers.CharField()
    value = serializers.FloatField()


class SKUCountryReportSerializer(serializers.Serializer):
    sku = serializers.CharField()
    statistics = CountryReportSerializer(many=True)


class AnswerReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()


class AnswerPerCountryReportSerializer(serializers.Serializer):
    sku = serializers.CharField()
    statistics = CountryReportSerializer(many=True)


class AnswerPerCityReportSerializer(serializers.Serializer):
    sku = serializers.CharField()
    statistics = CityReportSerializer(many=True)