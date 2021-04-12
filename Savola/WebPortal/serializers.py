from rest_framework import serializers
from WebPortal.models import *
from django.contrib.auth.models import User

from WebPortal.models import CustomUser

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         return token

# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'role')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )

        
#         user.set_password(validated_data['password'])
#         user.save()

#         return user
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ('photo_file_name',
#                   'nationality',
#                   'country',
#                   'city',
#                   'date_of_birth',
#                   'contact_number',
#                   'role',
#                   'username',
#                   'email',
#                   'password')
#     def create(self,username,email,password):
#         user = User.objects.create_user(username, email, password)
#         return user
        
from WebPortal.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "all"

class QuestionnaireTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnaireType
        fields = "__all__" 

# class QuestionnaireSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Questionnaires
#         fields = "__all__"

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
        

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveys
        fields = "__all__"

class SurveyActivitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyActivities
        fields = "__all__"

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"
