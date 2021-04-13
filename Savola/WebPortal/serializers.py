from rest_framework import serializers
from WebPortal.models import *

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login,logout


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','password','full_name','role','date_of_birth','contact_number','username','profile_pic','nationality')

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

class QuestionnaireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireType
        fields = "__all__" 

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaires
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOptions
        fields = "__all__"

        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = "__all__"

class RetailersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailers
        fields = "__all__"

class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"

class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = "__all__"
        

# class SurveySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Surveys
#         fields = "__all__"

class SurveyActivitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyActivities
        fields = "__all__"

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"
