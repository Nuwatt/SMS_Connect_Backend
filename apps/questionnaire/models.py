from django.db import models

from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.localize.models import Country, City, Area
from apps.user.models import AgentUser


class QuestionnaireType(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Questionnaire(BaseModel):
    REPEAT_CYCLE_CHOICES = (
        ('none', 'None'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    )
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=200)
    questionnaire_type = models.ForeignKey(QuestionnaireType, on_delete=models.CASCADE)
    country = models.ManyToManyField(Country)
    city = models.ManyToManyField(City)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    repeat_cycle = models.CharField(
        choices=REPEAT_CYCLE_CHOICES,
        max_length=9,
        default='none'
    )
    tags = models.ManyToManyField(AgentUser, blank=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='QU', model=Questionnaire)
        super(Questionnaire, self).save(*args, **kwargs)
