from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from apps.core.serializer_fields import PhoneNumberField
from apps.core.serializers import IdNameSerializer
from apps.localize.models import Country
from apps.user.models import PortalUser, Role
from apps.user.serializers.base_serializers import UserSerializer, UserLoginSerializer, UserLoginResponseSerializer, \
    AvatarSerializer
from apps.user.validators import validate_username, validate_date_of_birth

User = get_user_model()


class PortalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalUser
        fields = '__all__'


class ListPortalUserSerializer(serializers.Serializer):
    id = serializers.CharField()
    fullname = serializers.CharField(source='user.fullname')
    nationality = serializers.CharField(source='user.nationality')
    position = serializers.CharField()
    role = serializers.CharField()
    date_of_birth = serializers.DateField(source='user.date_of_birth', format='%d-%m-%Y')
    contact_number = PhoneNumberField(source='user.contact_number')


class RegisterPortalUserSerializer(UserSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    position = serializers.CharField()
    username = serializers.CharField(validators=[validate_username])
    fullname = serializers.CharField()
    avatar = serializers.ImageField(required=False)

    class Meta(UserSerializer.Meta):
        fields = (
            'email',
            'username',
            'password',
            'fullname',
            'nationality',
            'contact_number',
            'date_of_birth',
            'avatar',
            'position',
            'role',
        )


class PortalUserDetailSerializer(ListPortalUserSerializer):
    avatar = serializers.ImageField(source='user.avatar')
    email = serializers.EmailField(source='user.email')
    nationality = IdNameSerializer(source='user.nationality')
    role = IdNameSerializer()
    position = serializers.CharField()
    username = serializers.CharField(source='user.username')


class UpdatePortalUserSerializer(serializers.Serializer):
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
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    position = serializers.CharField()
    avatar = serializers.ImageField(required=False)

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


class PortalUserLoginSerializer(UserLoginSerializer):
    pass


class PortalUserLoginResponseSerializer(UserLoginResponseSerializer):
    role = serializers.SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=serializers.CharField())
    def get_role(self, instance):
        user = instance.get('detail')
        return user.portaluser.role.name


class UploadPortalUserAvatarSerializer(AvatarSerializer):
    pass
