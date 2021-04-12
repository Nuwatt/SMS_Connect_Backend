from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from .serializers import*
from django.contrib.auth import authenticate, login,logout
from .models import *

# Create your views here.
class UserSignupView(APIView):
    serializer_class = UserSignupSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if valid:
            serializer.save()
            response = {
                'success': True,
                'data':serializer.data,
                'status': status.HTTP_201_CREATED,
                'message': 'Signup Successfull!',
            }

            return Response(response)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:

            response = {
                'success': True,
                'status': status.HTTP_200_OK,
                'message': 'Login Success!',
                'access_token': serializer.data['access_token'],
                'refresh_token': serializer.data['refresh_token'],
                'user':serializer.data['email']
            }

            return Response(response)
