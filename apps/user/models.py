from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.user.managers import UserManager


class User(AbstractUser):
    username = None
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


class BaseUser(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )

    def __str__(self):
        return self.id

    class Meta:
        abstract = True


class AgentUser(BaseUser):
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='FW', model=AgentUser)
        super(AgentUser, self).save(*args, **kwargs)


class PortalUser(BaseUser):
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='PU', model=PortalUser)
        super(PortalUser, self).save(*args, **kwargs)
