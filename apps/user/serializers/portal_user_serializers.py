from rest_framework import serializers

from apps.user.models import PortalUser


class PortalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalUser
        fields = '__all__'


class ListPortalUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
