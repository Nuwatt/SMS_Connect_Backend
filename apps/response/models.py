from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core import fields
from apps.core.models import BaseModel
from apps.core.utils import generate_custom_id
from apps.core.validators import validate_latitude, validate_longitude
from apps.market.models import Retailer, Store
from apps.question.models import Question, QuestionOption, QuestionTypeChoice
from apps.questionnaire.models import Questionnaire
from apps.response.utils import upload_answer_image_to
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
    store = models.ForeignKey(
        Store,
        null=True,
        on_delete=models.CASCADE
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
        validators=[validate_latitude]
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
        validators=[validate_longitude]
    )
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='R', model=Response)
        super(Response, self).save(*args, **kwargs)

    def clean(self):
        if self._state.adding:
            # 1. if has uncompleted response
            if Response.objects.filter(
                    agent=self.agent,
                    questionnaire=self.questionnaire,
                    store=self.store,
                    is_completed=False
            ):
                raise DjangoValidationError('Agent has uncompleted record of same questionnaire')

            # 2. retailer must be under agent operation
            if self.agent not in self.questionnaire.tags.all():
                if self.store.city not in self.agent.operation_city.all():
                    raise DjangoValidationError({
                        'retailer': _('Agent is not in operation on this retailer.')
                    })

    @property
    def coordinates(self):
        if self.longitude and self.latitude:
            return '{},{}'.format(
                self.latitude,
                self.longitude
            )
        return None

    @property
    def completed_duration(self):
        if self.completed_at:
            difference = self.completed_at - self.created
            minutes = int(divmod(difference.total_seconds(), 60)[0])
            return '{} min'.format(minutes)
        return None

    @property
    def number_of_answers(self):
        return self.answer_set.count()


class Answer(BaseModel):
    id = models.CharField(
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = generate_custom_id(initial='AN', model=Answer)
        super(Answer, self).save(*args, **kwargs)


class TextAnswer(BaseModel):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pk)


class NumericAnswer(BaseModel):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    numeric = models.FloatField()

    def __str__(self):
        return str(self.pk)


class ChoiceAnswer(BaseModel):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    choice = models.ForeignKey(QuestionTypeChoice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    def clean(self):
        question = self.answer.question
        # 1. check if question is choice type
        if question.question_type.has_default_choices:
            # 2. check if choice is from same question type
            if question.question_type != self.choice.question_type:
                raise DjangoValidationError({
                    'option': _('Choice is not from same question type.')
                })
        else:
            raise DjangoValidationError(_('Only Choice answer are allowed.'))


class OptionAnswer(BaseModel):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['answer', 'option'],
                name='unique_option_answer'
            )
        ]

    def clean(self):
        question = self.answer.question
        # 1. check if question is option_type
        if question.question_type.has_options:
            # 2. check if option is from same question
            if question != self.option.question:
                raise DjangoValidationError({
                    'option': _('Option is not from same question.')
                })
        else:
            raise DjangoValidationError(_('Only Option answer are allowed.'))


class ImageAnswer(BaseModel):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_answer_image_to)

    def __str__(self):
        return str(self.pk)

    def clean(self):
        if self.answer.question.question_type.name != 'Pictures':
            raise DjangoValidationError(_('Only Image answer are allowed.'))
