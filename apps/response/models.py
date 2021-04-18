from django.db import models

from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.question.models import Question
from apps.questionnaire.models import Questionnaire
from apps.user.models import AgentUser


class Response(BaseModel):
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='R', model=Response)
        super(Response, self).save(*args, **kwargs)


class Answer(BaseModel):
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='AN', model=Answer)
        super(Answer, self).save(*args, **kwargs)
