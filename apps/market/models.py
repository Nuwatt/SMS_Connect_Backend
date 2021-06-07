from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import City


class Channel(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Retailer(BaseModel):
    name = models.CharField(max_length=100)
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'retailer', 'city'],
                name='unique_store'
            )
        ]

    def __str__(self):
        return self.name
