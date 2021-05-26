from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.response import models


@admin.register(models.Response)
class ResponseAdmin(BaseModelAdmin):
    readonly_fields = (
        'agent',
        'questionnaire',
    )
    raw_id_fields = (
        'retailer',
    )


@admin.register(models.Answer)
class AnswerAdmin(BaseModelAdmin):
    readonly_fields = (
        'response',
        'question',
    )


@admin.register(models.ImageAnswer)
class ImageAnswerAdmin(BaseModelAdmin):
    readonly_fields = (
        'answer',
        'image',
    )


@admin.register(models.TextAnswer)
class TextAnswerAdmin(BaseModelAdmin):
    readonly_fields = (
        'answer',
        'text',
    )


@admin.register(models.NumericAnswer)
class NumericAnswerAdmin(BaseModelAdmin):
    readonly_fields = (
        'answer',
        'numeric',
    )


@admin.register(models.OptionAnswer)
class OptionAnswerAdmin(BaseModelAdmin):
    readonly_fields = (
        'answer',
        'option',
    )


@admin.register(models.ChoiceAnswer)
class ChoiceAnswerAdmin(BaseModelAdmin):
    readonly_fields = (
        'answer',
        'choice',
    )
