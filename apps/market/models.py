from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _

from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import City


class Channel(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if Channel.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Channel name already exists.')
            })


class Retailer(BaseModel):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

    def clean(self):
        # check for unique name for unarchived list
        if Retailer.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Retailer name already exists.')
            })

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'channel'],
                name='unique_retailer'
            )
        ]


class Store(BaseModel):
    name = models.CharField(max_length=100)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    city = models.ForeignKey(
        City,
        null=True,
        on_delete=models.CASCADE
    )

    def clean(self):
        # check for unique name for unarchived list
        if Store.objects.filter(name__iexact=self.name, is_archived=False).exists():
            raise DjangoValidationError({
                'name': _('Store name already exists.')
            })

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'retailer', 'city'],
                name='unique_store'
            )
        ]

    def __str__(self):
        return self.name
