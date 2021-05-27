from rest_framework import serializers


class SKUMinMaxReportSerializer(serializers.Serializer):
    sku = serializers.CharField()
    max = serializers.FloatField()
    min = serializers.FloatField()
    mode = serializers.FloatField()
    mean = serializers.FloatField()
