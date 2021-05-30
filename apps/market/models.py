from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import Country, City


class Channel(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Retailer(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        null=True
    )
    country = models.ForeignKey(
        Country,
        null=True,
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Store(BaseModel):
    name = models.CharField(max_length=100)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
