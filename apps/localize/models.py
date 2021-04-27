from django.db import models

from apps.core.mixins import CoordinatesModelMixin
from apps.core.models import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'

class Country(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

        # 1. avoid duplicate country in same region
        constraints = [
            models.UniqueConstraint(
                fields=['region', 'name'],
                name='unique_country'
            )
        ]


class City(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        # 1. avoid duplicate city in same country
        constraints = [
            models.UniqueConstraint(
                fields=['country', 'name'],
                name='unique_city'
            )
        ]


class Area(BaseModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


