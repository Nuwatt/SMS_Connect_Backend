from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from apps.core.serializer_fields import PhoneNumberField
from apps.core.serializers import IdNameSerializer
from apps.core.validators import validate_image
from apps.localize.models import City, Country
from apps.user.models import AgentUser
from apps.user.serializers.base_serializers import (
    UserSignupSerializer,
    UserDetailSerializer,
    UserSerializer,
    UserLoginSerializer,
    UserLoginResponseSerializer,
    AvatarSerializer
)
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
    avatar = serializers.ImageField(validators=[validate_image], required=False)

    default_error_messages = {
        'empty_operation_country': 'Empty Operation Country is not allowed.'
    }

    class Meta(UserSignupSerializer.Meta):
        fields = UserSignupSerializer.Meta.fields + (
            'avatar',
            'operation_city',
            'operation_country'
        )

    def validate_operation_country(self, data):
        if len(data) == 0:
            self.fail('empty_operation_country')
        return data


class AgentUserProfileSerializer(UserDetailSerializer):
    pass


class UpdateAgentUserProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'fullname',
            'contact_number',
            'date_of_birth',
            'nationality',
            'avatar'
        )


class AgentUserDetailSerializer(ListAgentUserSerializer):
    avatar = serializers.ImageField(source='user.avatar')
    email = serializers.EmailField(source='user.email')
    nationality = IdNameSerializer(source='user.nationality')
    date_of_birth = serializers.DateField(source='user.date_of_birth')
    contact_number = serializers.CharField(source='user.contact_number')
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
    operation_city = serializers.PrimaryKeyRelatedField(many=True, queryset=City.objects.all())
    operation_country = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())
    avatar = serializers.ImageField(validators=[validate_image], required=False)

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


class BasicListAgentUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField(source='user.username')
