from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_serializer_method

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.core.serializers import IdNameSerializer
from apps.user import utils

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(UserSerializer):
    nationality = IdNameSerializer()
    id = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = (
            'id',
            'email',
            'username',
            'fullname',
            'avatar',
            'contact_number',
            'date_of_birth',
            'nationality',
        )

    @swagger_serializer_method(serializer_or_field=serializers.CharField())
    def get_id(self, instance):
        if instance.is_agent_user:
            return instance.agentuser.id
        elif instance.is_portal_user:
            return instance.portaluser.id


class UserSignupSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'email',
            'username',
            'password',
            'fullname',
            'nationality',
            'date_of_birth',
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password"
        }
    )


class UserLoginResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    detail = UserDetailSerializer()


class RegisterUserResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField(source='user.id')
    username = serializers.CharField(source='user.username')
    token = serializers.CharField()


class UidAndTokenSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        "invalid_token": _('Invalid token'),
        "invalid_uid": _('Invalid uid'),
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)

        # uid validation have to be here, because validate_<field_name>
        # doesn't work with modelserializer
        try:
            uid = utils.decode_uid(self.initial_data.get("uid", ""))
            self.user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            key_error = "invalid_uid"
            raise ValidationError(
                {"uid": [self.error_messages[key_error]]}, code=key_error
            )

        is_token_valid = default_token_generator.check_token(
            self.user, self.initial_data.get("token", "")
        )
        if is_token_valid:
            return validated_data
        else:
            key_error = "invalid_token"
            raise ValidationError(
                {"token": [self.error_messages[key_error]]}, code=key_error
            )


class PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, attrs):
        user = self.context["request"].user or self.user
        # why assert? There are ValidationError / fail everywhere
        assert user is not None

        try:
            validate_password(attrs["new_password"], user)
        except ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)


class PasswordResetConfirmSerializer(UidAndTokenSerializer, PasswordSerializer):
    pass


class PasswordResetSerializer(serializers.Serializer):
    """
    Use this to reset password
    """
    email = serializers.EmailField()

    default_error_messages = {
        'invalid_email': _('Invalid email.'),
    }

    def validate_email(self, data):
        try:
            self.user = User.objects.get(
                email=data
            )
        except User.DoesNotExist:
            self.fail('invalid_email')

        if self.user.has_usable_password():
            return data
        self.fail('invalid_email')


class ChangePasswordSerializer(PasswordSerializer):
    current_password = serializers.CharField(
        read_only=True,
        style={"input_type": "password"}
    )

    default_error_messages = {
        "invalid_password": _('Invalid current password.')
    }

    def validate_current_password(self, value):
        is_password_valid = self.context["request"].user.check_password(value)
        if is_password_valid:
            return value
        else:
            self.fail("invalid_password")


class SupportSerializer(serializers.Serializer):
    text = serializers.CharField()
    fullname = serializers.CharField()
    email = serializers.EmailField()


class AvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField()
