from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.user.managers import UserManager, AgentUserManager, PortalUserManager


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    contact_number = fields.PhoneNumberField()
    date_of_birth = models.DateField(null=True)
    avatar = models.ImageField(
        upload_to='avatar/',
        default="default_avatar.png",
    )
    is_agent_user = models.BooleanField(
        _('agent user'),
        default=False,
        help_text=_(
            'Designates whether this user is agent or not. '
            'Unselect this if user is not a agent.'
        ),
    )
    is_portal_user = models.BooleanField(
        _('portal user'),
        default=False,
        help_text=_(
            'Designates whether this user is portal user or not. '
            'Unselect this if user is not a portal user.'
        ),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def clean(self):
        # 1. user cannot be portal user and agent user at once
        if self.is_portal_user and self.is_agent_user:
            raise DjangoValidationError(
                _('User can\'t be portal user and agent at once')
            )

        django_user = bool(self.is_superuser or self.is_staff)

        if self.is_portal_user and django_user:
            raise DjangoValidationError(
                _('User can\'t be portal user and django user at once')
            )

        if self.is_agent_user and django_user:
            raise DjangoValidationError(
                _('User can\'t be agent user and django user at once')
            )


class AgentUser(User):
    objects = AgentUserManager()

    class Meta:
        proxy = True


class PortalUser(User):
    objects = PortalUserManager()

    class Meta:
        proxy = True
