from rest_framework import serializers

from apps.user.models import PortalUser, Role
from apps.user.serializers.base_serializers import UserSignupSerializer


class PortalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalUser
        fields = '__all__'


class ListPortalUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')


class RegisterPortalUserSerializer(UserSignupSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta(UserSignupSerializer.Meta):
        fields = UserSignupSerializer.Meta.fields + (
            'role',
        )
