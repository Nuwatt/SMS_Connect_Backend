from rest_framework import serializers


class MessageResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class IdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

