from rest_framework import serializers

from apps.user.models import AgentUser
from apps.user.serializers.base_serializers import UserSignupSerializer


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentUser
        fields = '__all__'


class ListAgentUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')


class RegisterAgentUserSerializer(UserSignupSerializer):
    pass
