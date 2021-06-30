from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def clean(self):
        # check for unique name for unarchived list
        if Country.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Country name already exists.')
            })


class City(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Nationality(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nationality'
        verbose_name_plural = 'Nationalities'

    def clean(self):
        # check for unique name for unarchived list
        if Nationality.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Nationality name already exists.')
            })
