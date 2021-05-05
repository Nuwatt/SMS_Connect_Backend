from rest_framework import serializers

from apps.core.validators import validate_csv_file


class MessageResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class IdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class IdCharSerializer(serializers.Serializer):
    id = serializers.CharField()


class IdIntegerSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class CSVFileInputSerializer(serializers.Serializer):
    file = serializers.FileField(validators=[validate_csv_file])
