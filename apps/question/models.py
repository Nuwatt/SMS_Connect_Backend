from django.db import models

from apps.core.utils import generate_custom_id
from apps.product.models import SKU, Brand
from apps.core.models import BaseModel
from apps.questionnaire.models import Questionnaire


class QuestionType(BaseModel):
    """
    Question Type model
    """
    name = models.CharField(
        max_length=244,
    )

    def __str__(self):
        return self.name


class QuestionStatement(BaseModel):
    """
    Question Statement model
    """
    statement = models.CharField(
        max_length=244,
    )

    def __str__(self):
        return self.statement


class Question(BaseModel):
    """
    Question model
    """
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    questionnaire = models.ForeignKey(
        Questionnaire,
        null=True,
        on_delete=models.CASCADE
    )
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question_statement = models.ForeignKey(QuestionStatement, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='Q', model=Question)
        super(Question, self).save(*args, **kwargs)


class QuestionOption(BaseModel):
    """
    Question Option model
    """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=True
    )
    option = models.CharField(
        max_length=244,
    )
