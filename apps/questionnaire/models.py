from django.db import models

from apps.core.models import BaseModel
from apps.localize.models import Country, City, Area


class QuestionnaireType(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Questionnaire(BaseModel):
    name = models.CharField(max_length=200)
    questionnaire_type = models.ForeignKey(QuestionnaireType, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
