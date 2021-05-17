from rest_framework import serializers

from apps.response.models import Response


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class StartQuestionnaireSerializer(ResponseSerializer):
    class Meta(ResponseSerializer.Meta):
        fields = (
            'retailer',
            'latitude',
            'longitude'
        )
