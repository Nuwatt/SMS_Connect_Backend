from django.db import models

from apps.core.mixins import CoordinatesModelMixin
from apps.core.models import BaseModel


class Retailer(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Store(BaseModel, CoordinatesModelMixin):
    name = models.CharField(max_length=100)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
