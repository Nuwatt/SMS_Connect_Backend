from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.localize.models import Country, City, Area
from apps.product.models import Category
from apps.user.models import AgentUser


class QuestionnaireType(BaseModel):
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='QUT', model=QuestionnaireType)
        super(QuestionnaireType, self).save(*args, **kwargs)


class Questionnaire(BaseModel):
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=200)
    questionnaire_type = models.ForeignKey(QuestionnaireType, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE
    )
    city = models.ManyToManyField(City)
    can_repeat = models.BooleanField(default=False)
    repeat_cycle = models.DurationField(
        null=True,
        blank=True,
        default=timedelta(weeks=0),
        help_text=_('Repeat Cycle in week, ex: 1 week , 2 week and so on.')
    )
    tags = models.ManyToManyField(AgentUser, blank=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self.repeat_cycle and (self.repeat_cycle > timedelta(weeks=0)):
            self.can_repeat = True
        else:
            self.can_repeat = False

        if self._state.adding:
            self.id = generate_custom_id(initial='QU', model=Questionnaire)
        super(Questionnaire, self).save(*args, **kwargs)

    def has_access_for_agent(self, agent):
        if agent not in self.tags.all():
            if not any(item in self.city.all() for item in agent.operation_city.all()):
                return False
        return True
