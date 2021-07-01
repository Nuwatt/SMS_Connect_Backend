from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

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
    has_default_choices = models.BooleanField(default=False)
    has_options = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def clean(self):
        # 1. check if both are true
        if self.has_default_choices and self.has_options:
            raise DjangoValidationError([
                DjangoValidationError({'has_default_choices': _('Cann\'t be True if has_options is True.')}),
                DjangoValidationError({'has_options': _('Cann\'t be True if has_default_choices is True.')}),
            ])


class QuestionTypeChoice(BaseModel):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return self.choice

    def clean(self):
        # 1. check if question_type has_default_choices
        if not self.question_type.has_default_choices:
            raise DjangoValidationError({
                'question_type': _('Question Type\'s has_default_choices is not been set.')
            })


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
    statement = models.CharField(max_length=255)
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
        null=True,
        limit_choices_to={'question_type__has_options': True}
    )
    option = models.CharField(
        max_length=244,
    )

    def clean(self):
        # 1. check if question_type has_default_choices
        if not self.question.question_type.has_options:
            raise DjangoValidationError({
                'question': _('Question has already default choices.')
            })
