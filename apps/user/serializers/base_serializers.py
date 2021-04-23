from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'id',
            'email',
            'first_name',
            'last_name'
        )


class UserSignupSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = (
            'email',
            'username',
            'password',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
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
