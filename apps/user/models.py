import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.user.managers import UserManager


class User(AbstractUser):
    ROLE_CHOICES = (
        ('1', 'Admin'),
        ('2', 'User'),
    )
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    contact_number = fields.PhoneNumberField()
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        default=2
    )
    date_of_birth = models.DateField(null=True)
    avatar = models.ImageField(
        upload_to='avatar/',
        default="default_avatar.png",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username
