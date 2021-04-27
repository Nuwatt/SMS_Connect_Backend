from rest_framework import serializers

from apps.user.models import PortalUser, Role
from apps.user.serializers.base_serializers import UserSignupSerializer


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ListRoleSerializer(RoleSerializer):
    class Meta(RoleSerializer.Meta):
        fields = (
            'id',
            'name',
        )


class AddRoleSerializer(RoleSerializer):
    class Meta(RoleSerializer.Meta):
        fields = (
            'name',
        )
