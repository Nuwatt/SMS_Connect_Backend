from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

#Table18 User role Table
class Roles(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)

# #Table1 UserTable
# class Users(User):
#     status = models.BooleanField(default=True)
#     isDeleted = models.BooleanField(default=False)
#     created = models.DateTimeField(default=datetime.now, blank=True)
#     updated = models.DateTimeField(default=datetime.now, blank=True)
#     user_id = models.AutoField(primary_key=True)
#     photo_file_name = models.CharField(max_length=100)
#     nationality = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     contact_number = models.CharField(max_length=12)
#     role = models.ForeignKey(Roles,on_delete=models.CASCADE)
#     # display_name = models.CharField(max_length=100,unique=True) #email ID of user to login
#     # password = models.CharField(max_length=50)
#     # role = models.CharField(max_length=50)




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    photo_file_name = models.CharField(default="avatar.png",max_length=100)
    nationality = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    contact_number = models.CharField(max_length=12)
    # role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.email
        
# class Profile(models.Model):
#     user_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
#     photo_file_name = models.CharField(default="avatar.png",max_length=100)
#     nationality = models.CharField(max_length=100, null=False)
#     country = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     date_of_birth = models.DateField(null=True)
#     contact_number = models.CharField(max_length=12)
#     role = models.ForeignKey(Roles,on_delete=models.CASCADE)


#Table 15 Category table
class Category(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

#Table 16 Brands table
class Brands(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

#Table 17 Category table
class Sku(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    sku_id = models.AutoField(primary_key=True)
    sku_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)

#Table 4 Questionnaire type table
class QuestionnaireType(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    questionnaire_type_id = models.AutoField(primary_key=True)
    questionnaire_type = models.CharField(max_length=100)
    # Questionnaire = models.CharField(max_length=100) # Questionnaire id of Questionnaire table
    
#Table 6 Question table
class Questions(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    questions_id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length=100)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku,on_delete=models.CASCADE)
    # QuestionStatement = models.CharField(max_length=100) # Questionnaire Statement Id of QS table
    # QuestionOption = models.CharField(max_length=100) # Question Options coming from qo table

#Table5 Questionnaire table
class Questionnaires(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    questionnaire_id = models.AutoField(primary_key=True)
    questionnaire_name = models.CharField(max_length=100) # name display on App carasoul
    questionnaire_type = models.ForeignKey(QuestionnaireType,on_delete=models.CASCADE) #Id of questionnaire type table
    question = models.ForeignKey(Questions,on_delete=models.CASCADE) # id of question table, one to many dbt delete?


#Table 7 Question options (QO) table
class QuestionOptions(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    question_options_id = models.AutoField(primary_key=True)
    question_options = models.CharField(max_length=100)
    
#Table 8 QS
class QuestionStatments(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    question_statment_id = models.AutoField(primary_key=True)
    question_statement = models.CharField(max_length=100)
    question_options = models.OneToOneField(QuestionOptions,on_delete=models.CASCADE) # Id from QO table
    question = models.ForeignKey(Questions,on_delete=models.CASCADE) #? dbt... delete

#Table 10 Country table
class Country(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100) # latitude of the postion from backend
    longitude = models.CharField(max_length=100)

#Table 11 Country table
class City(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100) # latitude of the postion from backend
    longitude = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) # countryid from country table

#Table 12 Country table
class Areas(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100) # latitude of the postion from backend
    longitude = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) # countryid from country table
    city = models.ForeignKey(City,on_delete=models.CASCADE) # Cityid from city table

#Table 13 Retailer Table
class Retailers(models.Model):    
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    retailer_id = models.AutoField(primary_key=True)
    reatailer_name = models.CharField(max_length=100)

#Table 14 Store table
class Stores(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3)
    retailer = models.ForeignKey(Retailers,on_delete=models.CASCADE)


#Table2 Survey Table
class Surveys(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    time_submited = models.DateTimeField(default=datetime.now) #time of survey submited by agent    #to calculate the estimated time taken for 
    survey_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) #country Table id multy select
    city = models.ForeignKey(City,on_delete=models.CASCADE) #city Table id all cityes under selected city shoould display here
    area = models.ForeignKey(Areas,on_delete=models.CASCADE) 
    category = models.ManyToManyField(Category)#category table id
    brand = models.ManyToManyField(Brands)
    store = models.ForeignKey(Stores,on_delete=models.CASCADE)
    retaier = models.ForeignKey(Retailers,on_delete=models.CASCADE)
    frequency = models.CharField(max_length=100) #for repeat this survey by a time interval

#Table3 Survey Acivity table
class SurveyActivities(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    survey_activity_id = models.AutoField(primary_key=True)
    survey = models.OneToOneField(Surveys,on_delete=models.CASCADE) # id of survey table
    user = models.ManyToManyField(CustomUser) #usertable id
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3) #longitude and latitude of the user send by app while they do this survey


#Table 9 answer table
class Answers(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    answer_id = models.AutoField(primary_key=True)
    question = models.OneToOneField(Questions,on_delete=models.CASCADE) #Question id of q table
    survey = models.ForeignKey(Surveys,on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaires,on_delete=models.CASCADE) #Questionnaire id of questionnaire table
    answer = models.CharField(max_length=100)



