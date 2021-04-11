from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login

from WebPortal.models import *
from WebPortal.serializers import *

# views.

# from django.urls import reverse
# from users.forms import CustomUserCreationForm


# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "users/register.html",
#             {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("dashboard"))

#Api for create, delete,update a user role (roles table data )

# from .serializers import MyTokenObtainPairSerializer
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth.models import User
# from .serializers import RegisterSerializer
# from rest_framework import generics



# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer

@csrf_exempt
def rolesApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            table_data = Roles.objects.all()
            table_serializer = RolesSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else:
            raw_data = Roles.objects.get(role_id=id)
            table_serializer = RolesSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = RolesSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Roles.objects.get(role_id=form_data['role_id'])
        table_serializer = RolesSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        form_data = Roles.objects.get(role_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

#UserApi for create,List, Delete and Edit Users
@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        if id == 0: #to get detailes of all users
            users = Users.objects.all()
            user_serializer = UserSerializer(users, many=True)
            return JsonResponse(user_serializer.data, safe=False)
        else:    #Filter User by Id
            user = Users.objects.get(user_id=id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)

    elif request.method=='POST': # Create new user
        user_data=JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        print(user_serializer)
        if user_serializer.is_valid():
            # new_user = user_serializer.create(username=user_data['username'], email=user_data['email'], password=user_data['password'])
            # new_user.photo_file_name = user_data['photo_file_name']
            # new_user.nationality = user_data['nationality']
            # new_user.country = user_data['country']
            # new_user.city = user_data['city']
            # new_user.date_of_birth = user_data['date_of_birth']
            # new_user.contact_number = user_data['contact_number']
            # new_user.save()
            user_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT': # Update existing user
        user_data = JSONParser().parse(request)
        user=Users.objects.get(user_id=user_data['user_id'])
        user_serializer=UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': # Delete a Specific user by ID
        user=Users.objects.get(user_id=id)
        user.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


# Question Options -> Question Statment -> Question -> ///Questionnaire\\\ <- Question Type 
#Api for create, delete,update and get by id of Questionnaire table data 
@csrf_exempt
def questionnairesApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            table_data = Questionnaires.objects.all()
            table_serializer = QuestionnaireSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else:
            raw_data = Questionnaires.objects.get(questionnaire_id=id)
            table_serializer = QuestionnaireSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = QuestionnaireSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Questionnaires.objects.get(questionnaire_id=form_data['questionnaire_id'])
        table_serializer = QuestionnaireSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        form_data = Questionnaires.objects.get(questionnaire_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Questions table data 
@csrf_exempt
def questionsApi(request,id=0):
    if request.method == 'GET':
        if id == 0:
            table_data = Questions.objects.all()
            table_serializer = QuestionSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Questions.objects.get(questions_id=id)
            table_serializer = QuestionSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = QuestionSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Questions.objects.get(questions_id=form_data['questions_id'])
        table_serializer = QuestionSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        form_data = Questions.objects.get(questions_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Questionnaire Type (consumer,retailer,stock and price) table data 
@csrf_exempt
def questionnaireTypeApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            table_data = QuestionnaireType.objects.all()
            table_serializer = QuestionnaireTypeSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = QuestionnaireType.objects.get(questionnaire_type_id=id)
            table_serializer = QuestionnaireTypeSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST': 
        form_data = JSONParser().parse(request)
        table_serializer = QuestionnaireTypeSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = QuestionnaireType.objects.get(questionnaire_type_id=form_data['questionnaire_type_id'])
        table_serializer = QuestionnaireTypeSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        form_data = QuestionnaireType.objects.get(questionnaire_type_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Question options (for save options) table data 
@csrf_exempt
def questionOptionsApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = QuestionOptions.objects.all()
            table_serializer = QuestionOptionSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else:   
            raw_data = QuestionOptions.objects.get(question_options_id=id)
            table_serializer = QuestionOptionSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = QuestionOptionSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT': 
        form_data = JSONParser().parse(request)
        table_data = QuestionOptions.objects.get(question_options_id=form_data['question_options_id'])
        table_serializer = QuestionOptionSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        form_data = QuestionOptions.objects.get(question_options_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

#Api for create, delete,update and get by id of Question statement (mainly for branching questions) table data 
@csrf_exempt
def questionStatmentaApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = QuestionStatments.objects.all()
            table_serializer = QuestionStatementSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = QuestionStatments.objects.get(question_statment_id=id)
            table_serializer = QuestionStatementSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = QuestionStatementSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = QuestionStatments.objects.get(question_statment_id=form_data['question_statment_id'])
        table_serializer = QuestionStatementSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = QuestionStatments.objects.get(question_statment_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# Survey Activity -> Survey Table <-> Questionnaire Table <- Answer Table
#Api for create, delete,update and get by id of Survey table data 
@csrf_exempt
def surveyApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Surveys.objects.all()
            table_serializer = SurveySerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Surveys.objects.get(survey_id=id)
            table_serializer = SurveySerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = SurveySerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Surveys.objects.get(survey_id=form_data['survey_id'])
        table_serializer = SurveySerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Surveys.objects.get(survey_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

#Api for create, delete,update and get by id of Survey Activity table data 
@csrf_exempt
def surveyActivityApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = SurveyActivities.objects.all()
            table_serializer = SurveyActivitieSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = SurveyActivities.objects.get(survey_activity_id=id)
            table_serializer = SurveyActivitieSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = SurveyActivitieSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = SurveyActivities.objects.get(survey_activity_id=form_data['survey_activity_id'])
        table_serializer = SurveyActivitieSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = SurveyActivities.objects.get(survey_activity_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Answer table data 
@csrf_exempt
def answerApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Answers.objects.all()
            table_serializer = AnswerSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Answers.objects.get(answer_id=id)
            table_serializer = AnswerSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = AnswerSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Answers.objects.get(answer_id=form_data['answer_id'])
        table_serializer = AnswerSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Answers.objects.get(answer_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# Country <- City <- Area
#Api for create, delete,update and get by id of Country table data 
@csrf_exempt
def countryApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Country.objects.all()
            table_serializer = CountrySerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Country.objects.get(country_id=id)
            table_serializer = CountrySerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = CountrySerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Country.objects.get(country_id=form_data['country_id'])
        table_serializer = CountrySerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Country.objects.get(country_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of City table data 
@csrf_exempt
def cityApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = City.objects.all()
            table_serializer = CitySerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = City.objects.get(city_id=id)
            table_serializer = CitySerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = CitySerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = City.objects.get(city_id=form_data['city_id'])
        table_serializer = CitySerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = City.objects.get(city_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Area table data 
@csrf_exempt
def areaApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Areas.objects.all()
            table_serializer = AreasSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Areas.objects.get(area_id=id)
            table_serializer = AreasSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = AreasSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Areas.objects.get(area_id=form_data['area_id'])
        table_serializer = AreasSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Areas.objects.get(area_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

# Retailer -> Store 
#Api for create, delete,update and get by id of Retailer table data 
@csrf_exempt
def retailerApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Retailers.objects.all()
            table_serializer = RetailersSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Retailers.objects.get(retailer_id=id)
            table_serializer = RetailersSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = RetailersSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Retailers.objects.get(retailer_id=form_data['retailer_id'])
        table_serializer = RetailersSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Retailers.objects.get(retailer_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Store table data 
@csrf_exempt
def storeApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Stores.objects.all()
            table_serializer = StoresSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Stores.objects.get(store_id=id)
            table_serializer = StoresSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = StoresSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Stores.objects.get(store_id=form_data['store_id'])
        table_serializer = StoresSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Stores.objects.get(store_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


# Sku -> Brand -> Category
#Api for create, delete,update and get by id of Category table data 
@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Category.objects.all()
            table_serializer = CategorySerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Category.objects.get(category_id=id)
            table_serializer = CategorySerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = CategorySerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Category.objects.get(category_id=form_data['category_id'])
        table_serializer = CategorySerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Category.objects.get(category_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Brand table data 
@csrf_exempt
def brandApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Brands.objects.all()
            table_serializer = BrandsSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Brands.objects.get(brand_id=id)
            table_serializer = BrandsSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = BrandsSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Brands.objects.get(brand_id=form_data['brand_id'])
        table_serializer = BrandsSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Brands.objects.get(brand_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#Api for create, delete,update and get by id of Sku table data 
@csrf_exempt
def skuApi(request,id=0):
    if request.method=='GET':
        if id == 0: 
            table_data = Sku.objects.all()
            table_serializer = SkuSerializer(table_data, many=True)
            return JsonResponse(table_serializer.data, safe=False)
        else: 
            raw_data = Sku.objects.get(sku_Id=id)
            table_serializer = SkuSerializer(raw_data)
            return JsonResponse(table_serializer.data, safe=False)

    elif request.method=='POST':
        form_data = JSONParser().parse(request)
        table_serializer = SkuSerializer(data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        form_data = JSONParser().parse(request)
        table_data = Sku.objects.get(sku_id=form_data['sku_id'])
        table_serializer = SkuSerializer(table_data,data=form_data)
        if table_serializer.is_valid():
            table_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE': 
        form_data = Sku.objects.get(sku_id=id)
        form_data.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


# #Login Api 
@csrf_exempt
def loginApi(request):
#     # if request.method=='GET':
#     #     form_data = JSONParser().parse(request)
#     #     table_data = Users.objects.get(DisplayName=form_data['email'])
#     #     if table_data:
#     #         if table_data.Password == form_data['password']:
#     #             table_serializer = UserSerializer(table_data)
#     #             return JsonResponse("Login success full", safe=False)
#     #         else:
#     #             return JsonResponse("check your password", safe=False)
#     #     else:
#     #         return JsonResponse("login denied", safe=False)
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        print(username,password,user)
        if user is not None:
            login(request, user)
            return JsonResponse("Login success full", safe=False)
        else:
            return JsonResponse("login denied", safe=False)
                

