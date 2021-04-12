from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from rest_framework_simplejwt.tokens import RefreshToken

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

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True,null=True)
    is_active = models.BooleanField(default=True)
    role = models.PositiveSmallIntegerField(choices=choice_roles, blank=True, null=True, default=1)
    profile_pic = models.CharField(default="avatar.png",max_length=100)
    # nationality = models.CharField(max_length=100, null=False)
    # country = models.ManyToManyField()
    # city = models.ManyToManyField()
    date_of_birth = models.DateField(null=True)
    contact_number = models.CharField(max_length=12)
    username = models.CharField(max_length=100)

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


    def get_full_name(self):
        return self.first_name+self.last_name

    def get_short_name(self):
        return self.first_name

    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
