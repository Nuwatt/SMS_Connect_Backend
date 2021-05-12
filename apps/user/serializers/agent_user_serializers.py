from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.serializer_fields import PhoneNumberField
from apps.core.serializers import IdNameSerializer
from apps.localize.models import City, Country
from apps.user.models import AgentUser
from apps.user.serializers.base_serializers import UserSignupSerializer, UserDetailSerializer, UserSerializer, \
    UserLoginSerializer, UserLoginResponseSerializer, AvatarSerializer
from apps.user.validators import validate_date_of_birth

User = get_user_model()


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentUser
        fields = '__all__'


class ListAgentUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField(source='user.username')
    fullname = serializers.CharField(source='user.fullname')
    operation_city = serializers.ListSerializer(
        child=serializers.CharField()
    )
    operation_country = serializers.ListSerializer(
        child=serializers.CharField()
    )
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


class AgentUserDetailSerializer(ListAgentUserSerializer):
    avatar = serializers.ImageField(source='user.avatar')
    email = serializers.EmailField(source='user.email')
    nationality = IdNameSerializer(source='user.nationality')
    operation_city = IdNameSerializer(many=True)
    operation_country = IdNameSerializer(many=True)
    total_completed_questionnaire = None


class UpdateAgentUserSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    username = serializers.CharField(write_only=True)
    fullname = serializers.CharField(write_only=True)
    nationality = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        write_only=True
    )
    contact_number = PhoneNumberField(write_only=True)
    date_of_birth = serializers.DateField(
        validators=[validate_date_of_birth],
        write_only=True
    )
    avatar = serializers.ImageField(write_only=True)
    operation_city = serializers.PrimaryKeyRelatedField(many=True, queryset=City.objects.all())
    operation_country = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())

    default_error_messages = {
        'duplicate_email': _('Email already exists in another user.'),
        'duplicate_username': _('Username already exists in another user.'),
    }

    def validate_username(self, data):
        if self.instance.user.username != data:
            if User.objects.filter(username=data).exists():
                self.fail('duplicate_username')
        return data

    def validate_email(self, data):
        if self.instance.user.email != data:
            if User.objects.filter(email=data).exists():
                self.fail('duplicate_email')
        return data


class AgentUserLoginSerializer(UserLoginSerializer):
    pass


class AgentUserLoginResponseSerializer(UserLoginResponseSerializer):
    pass


class UploadAgentUserAvatarSerializer(AvatarSerializer):
    pass
