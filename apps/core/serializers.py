from rest_framework import serializers


class MessageResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class IdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class IdCharSerializer(serializers.Serializer):
    id = serializers.CharField()


class IdIntegerSerializer(serializers.Serializer):
    id = serializers.IntegerField()

