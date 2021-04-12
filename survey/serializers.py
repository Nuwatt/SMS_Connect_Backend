from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth import authenticate, login,logout




class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password','first_name','last_name','role','date_of_birth','contact_number')

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        print(User.objects.all())
        return new_user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Incorrect login credentials")

        try:
            user_token = RefreshToken.for_user(user)
            refresh_token = str(user_token)
            access_token = str(user_token.access_token)

            res = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'email': user.email,
            }

            return res

        except user.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
