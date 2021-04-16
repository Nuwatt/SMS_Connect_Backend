from django.db import models

from apps.product.models import SKU, Brand
from apps.core.models import BaseModel
from apps.question import validators


class QuestionType(BaseModel):
    """
    Question Type model
    """
    type = models.CharField(
        max_length=244,
        validators=[validators.validate_question_type]
    )

    def __str__(self):
        return self.type


class QuestionStatement(BaseModel):
    """
    Question Statement model
    """
    statement = models.CharField(
        max_length=244,
        validators=[validators.validate_question_statement]
    )

    def __str__(self):
        return self.statement


class Question(BaseModel):
    """
    Question model
    """
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question_statement = models.ForeignKey(QuestionStatement, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_statement.statement


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
        validators=[validators.validate_question_option]
    )

    def __str__(self):
        return self.option
