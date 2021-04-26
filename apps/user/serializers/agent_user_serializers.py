from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.core.serializers import IdNameSerializer
from apps.localize.models import City, Country
from apps.user.models import AgentUser
from apps.user.serializers.base_serializers import UserSignupSerializer, UserDetailSerializer, UserSerializer

User = get_user_model()


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentUser
        fields = '__all__'


class ListAgentUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField(source='user.username')
    fullname = serializers.CharField(source='user.fullname')
    email = serializers.EmailField(source='user.email')
    operation_city = IdNameSerializer(many=True)
    operation_country = IdNameSerializer(many=True)
    total_completed_questionnaire = serializers.IntegerField()


class RegisterAgentUserSerializer(UserSignupSerializer):
    operation_city = serializers.PrimaryKeyRelatedField(many=True, queryset=City.objects.all())
    operation_country = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())

    class Meta(UserSignupSerializer.Meta):
        fields = UserSignupSerializer.Meta.fields + (
            'avatar',
            'operation_city',
            'operation_country'
        )


class AgentUserProfileSerializer(UserDetailSerializer):
    pass


class UpdateAgentUserProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'fullname',
            'contact_number',
            'date_of_birth',
            'nationality',
        )
