from rest_framework import serializers


class OverviewReportSerializer(serializers.Serializer):
    field_work = serializers.IntegerField()
    questionnaire = serializers.IntegerField()
    answer = serializers.IntegerField()
