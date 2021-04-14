from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from rest_framework_simplejwt.tokens import RefreshToken

#Table18 User role Table
class Roles(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)

#Table 15 Category table
class Category(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.pk)

#Table 16 Brands table
class Brands(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __unicode__(self):
        return str(self.pk)

#Table 17 Category table
class Sku(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #sku_id = models.AutoField(primary_key=True)
    sku_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)

    def __unicode__(self):
        return [self.brand.name, self.category.name]

    class Meta:
        verbose_name_plural = "SKUs"

#Table 4 Questionnaire type table
class QuestionnaireType(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #questionnaire_type_id = models.AutoField(primary_key=True)
    questionnaire_type = models.CharField(max_length=100)
    # Questionnaire = models.CharField(max_length=100) # Questionnaire id of Questionnaire table
    
#Table 6 Question table
class Questions(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #questions_id = models.AutoField(primary_key=True)
    question_type = models.CharField(max_length=100)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku,on_delete=models.CASCADE)
    # QuestionStatement = models.CharField(max_length=100) # Questionnaire Statement Id of QS table
    # QuestionOption = models.CharField(max_length=100) # Question Options coming from qo table

# #Table5 Questionnaire table
# class Questionnaires(models.Model):
#     status = models.BooleanField(default=True)
#     isDeleted = models.BooleanField(default=False)
#     created = models.DateTimeField(default=datetime.now, blank=True)
#     updated = models.DateTimeField(default=datetime.now, blank=True)
##     questionnaire_id = models.AutoField(primary_key=True)
#     questionnaire_name = models.CharField(max_length=100) # name display on App carasoul
#     questionnaire_type = models.ForeignKey(QuestionnaireType,on_delete=models.CASCADE) #Id of questionnaire type table
#     question = models.ForeignKey(Questions,on_delete=models.CASCADE) # id of question table, one to many dbt delete?


#Table 7 Question options (QO) table
class QuestionOptions(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #question_options_id = models.AutoField(primary_key=True)
    question_options = models.CharField(max_length=100)
    

#Table 10 Country table
class Country(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3)

    def __unicode__(self):
        return str(self.pk)

#Table 11 City table
class City(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) # countryid from country table

    def __unicode__(self):
        return str(self.pk)

#Table 12 Country table
class Areas(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3)
    country = models.ForeignKey(Country,on_delete=models.CASCADE) # countryid from country table
    city = models.ForeignKey(City,on_delete=models.CASCADE) # Cityid from city table

class UserManager(BaseUserManager):

    def create_user(self, email, password=None,**kwargs):

        if email is None:
            raise TypeError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    choice_roles =(
    ('1','Admin'),
    ('2','User')
    )

    
    email = models.EmailField(unique=True,null=True)
    full_name = models.CharField(max_length=200)
    role = models.PositiveSmallIntegerField(choices=choice_roles, blank=True, null=True, default=1)
    date_of_birth = models.DateField(null=True)
    contact_number = models.CharField(max_length=12)
    username = models.CharField(max_length=100)
    profile_pic = models.CharField(default="avatar.png",max_length=100)
    nationality = models.CharField(max_length=100, null=False)
    # country = models.ManyToManyField(country)
    # city = models.ManyToManyField(city)

    is_staff = models.BooleanField(

            default=False,

        )
    is_active = models.BooleanField(

        default=True,

    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

#Table 13 Retailer Table
class Retailers(models.Model):    
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #retailer_id = models.AutoField(primary_key=True)
    reatailer_name = models.CharField(max_length=100)

#Table 14 Store table
class Stores(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3)
    retailer = models.ForeignKey(Retailers,on_delete=models.CASCADE)


#Table2 Questionnaire Table
class Questionnaires(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now, blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    time_submited = models.DateTimeField(default=datetime.now) #time of survey submited by agent    #to calculate the estimated time taken for 
    #survey_id = models.AutoField(primary_key=True)
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
    #survey_activity_id = models.AutoField(primary_key=True)
    questionnaire = models.OneToOneField(Questionnaires,on_delete=models.CASCADE) # id of survey table
    user = models.ManyToManyField(User) #usertable id
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    langitude = models.DecimalField(max_digits=8, decimal_places=3) #longitude and latitude of the user send by app while they do this survey


#Table 9 answer table
class Answers(models.Model):
    status = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=datetime.now,blank=True)
    updated = models.DateTimeField(default=datetime.now, blank=True)
    #answer_id = models.AutoField(primary_key=True)
    question = models.OneToOneField(Questions,on_delete=models.CASCADE) #Question id of q table
    Questionnaire = models.ForeignKey(Questionnaires,on_delete=models.CASCADE)
    # questionnaire = models.ForeignKey(Surveys,on_delete=models.CASCADE) #Questionnaire id of questionnaire table
    answer = models.CharField(max_length=100)



