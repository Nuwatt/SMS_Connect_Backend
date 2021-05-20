from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.localize.models import Country, City
from apps.user.managers import UserManager
from apps.user.utils import upload_avatar_to
from apps.user.validators import validate_date_of_birth, validate_username


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    fullname = models.CharField(_('fullname'), max_length=200, null=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        null=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[validate_username],
    )
    contact_number = fields.PhoneNumberField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, validators=[validate_date_of_birth])
    nationality = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        upload_to=upload_avatar_to,
        default="avatar/default_avatar.png",
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
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_archived = models.BooleanField(default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
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

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)


class Role(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


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
    operation_city = models.ManyToManyField(City)
    operation_country = models.ManyToManyField(Country)
    total_completed_questionnaire = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='FW', model=AgentUser)
        super(AgentUser, self).save(*args, **kwargs)


class PortalUser(BaseUser):
    position = models.CharField(max_length=200)
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=True
    )

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='PU', model=PortalUser)
        super(PortalUser, self).save(*args, **kwargs)
