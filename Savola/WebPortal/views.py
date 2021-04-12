from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from WebPortal.models import *
from WebPortal.serializers import *

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from django.contrib.auth import authenticate, login,logout


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

@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def rolesApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Roles.objects.all()
            serializer = Roles(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = RolesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Roles.objects.get(role_id=id)
        except Roles.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = RolesSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = RolesSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Roles.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)

# # Question Options -> Question Statment -> Question -> ///Questionnaire\\\ <- Question Type 
# #Api for create, delete,update and get by id of Questionnaire table data 
# @csrf_exempt
# @api_view(['GET', 'POST','DELETE','PUT'])
# def questionnairesApi(request,id=0):
#     if request.method=='GET':
#         if id == 0:
#             table_data = Questionnaires.objects.all()
#             table_serializer = QuestionnaireSerializer(table_data, many=True)
#             return JsonResponse(table_serializer.data, safe=False)
#         else:
#             raw_data = Questionnaires.objects.get(questionnaire_id=id)
#             table_serializer = QuestionnaireSerializer(raw_data)
#             return JsonResponse(table_serializer.data, safe=False)

#     elif request.method=='POST':
#         form_data = JSONParser().parse(request)
#         table_serializer = QuestionnaireSerializer(data=form_data)
#         if table_serializer.is_valid():
#             table_serializer.save()
#             return JsonResponse("Added Successfully!!" , safe=False)
#         return JsonResponse("Failed to Add.",safe=False)
    
#     elif request.method=='PUT':
#         form_data = JSONParser().parse(request)
#         table_data = Questionnaires.objects.get(questionnaire_id=form_data['questionnaire_id'])
#         table_serializer = QuestionnaireSerializer(table_data,data=form_data)
#         if table_serializer.is_valid():
#             table_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method=='DELETE':
#         form_data = Questionnaires.objects.get(questionnaire_id=id)
#         form_data.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Questions table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def questionsApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Questions.objects.all()
            serializer = QuestionSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = QuestionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Questions.objects.get(questions_id=id)
        except Questions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = QuestionSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = QuestionSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Questions.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


#Api for create, delete,update and get by id of Questionnaire Type (consumer,retailer,stock and price) table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def questionnaireTypeApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = QuestionnaireType.objects.all()
            serializer = QuestionnaireTypeSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = QuestionnaireTypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = QuestionnaireType.objects.get(questionnaire_type_id=id)
        except QuestionnaireType.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = QuestionnaireTypeSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = QuestionnaireTypeSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            QuestionnaireType.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)



#Api for create, delete,update and get by id of Question options (for save options) table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def questionOptionsApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = QuestionOptions.objects.all()
            serializer = QuestionOptionSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = QuestionOptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = QuestionOptions.objects.get(question_options_id=id)
        except QuestionOptions.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = QuestionOptionSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = QuestionOptionSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            QuestionOptions.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)

# Survey Activity -> Survey Table <-> Questionnaire Table <- Answer Table
#Api for create, delete,update and get by id of Survey table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def surveyApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Surveys.objects.all()
            serializer = SurveySerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = SurveySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Surveys.objects.get(survey_id=id)
        except Surveys.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = SurveySerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = SurveySerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Surveys.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


#Api for create, delete,update and get by id of Survey Activity table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def surveyActivityApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = SurveyActivities.objects.all()
            serializer = SurveyActivitieSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = SurveyActivitieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = SurveyActivities.objects.get(survey_activity_id=id)
        except SurveyActivities.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = SurveyActivitieSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = SurveyActivitieSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            SurveyActivities.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


#Api for create, delete,update and get by id of Answer table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def answerApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Answers.objects.all()
            serializer = AnswerSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Answers.objects.get(answer_id=id)
        except Answers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = AnswerSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = AnswerSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Answers.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


# Country <- City <- Area
#Api for create, delete,update and get by id of Country table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def countryApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Country.objects.all()
            serializer = CountrySerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CountrySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Country.objects.get(country_id=id)
        except Country.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = CountrySerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CountrySerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Country.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)



#Api for create, delete,update and get by id of City table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def cityApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = City.objects.all()
            serializer = CitySerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = City.objects.get(city_id=id)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = CitySerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CitySerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            City.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


#Api for create, delete,update and get by id of Area table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def areaApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Areas.objects.all()
            serializer = AreasSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = AreasSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Areas.objects.get(area_id=id)
        except Areas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = AreasSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = AreasSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Areas.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)

# Retailer -> Store 
#Api for create, delete,update and get by id of Retailer table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def retailerApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            data = Retailers.objects.all()
            serializer = RetailersSerializer(data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = RetailersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Retailers.objects.get(retailer_id=id)
        except Retailers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = RetailersSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = RetailersSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Retailers.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


#Api for create, delete,update and get by id of Store table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def storeApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            store_data = Stores.objects.all()
            serializer = StoresSerializer(store_data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = StoresSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Stores.objects.get(store_id=id)
        except Stores.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = StoresSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = StoresSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Stores.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


# Sku -> Brand -> Category
#Api for create, delete,update and get by id of Category table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def categoryApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            catagory_data = Category.objects.all()
            serializer = CategorySerializer(catagory_data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Category.objects.get(category_id=id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = CategorySerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CategorySerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Brands.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


#Api for create, delete,update and get by id of Brand table data 
@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def brandApi(request,id=0):
    if id == 0:
        if request.method == 'GET':
            brand_data = Brands.objects.all()
            serializer = BrandsSerializer(brand_data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = BrandsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Brands.objects.get(brand_id=id)
        except Brands.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = BrandsSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = BrandsSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Brands.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST','DELETE','PUT'])
def skuApi(request, id = 0):

    if id == 0:
        if request.method == 'GET':
            Sku_data = Sku.objects.all()
            serializer = SkuSerializer(Sku_data, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = SkuSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            pk = Sku.objects.get(sku_id=id)
        except Sku.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        if request.method == 'GET':
            serializer = SkuSerializer(pk)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = SkuSerializer(pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            Sku.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)

                

