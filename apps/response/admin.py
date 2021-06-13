from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.response import models


@admin.register(models.Response)
class ResponseAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'completed_at',
        'created'
    )
    readonly_fields = BaseModelAdmin.readonly_fields + (
        'agent',
        'questionnaire',
    )
    raw_id_fields = (
        'store',
    )


@admin.register(models.Answer)
class AnswerAdmin(BaseModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields + (
        'response',
        'question',
    )


@admin.register(models.ImageAnswer)
class ImageAnswerAdmin(BaseModelAdmin):
    readonly_fields = BaseModelAdmin.readonly_fields + (
        'answer',
        'image',
    )


@admin.register(models.TextAnswer)
class TextAnswerAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'text',
    )
    readonly_fields = BaseModelAdmin.readonly_fields + (
        'answer',
        'text',
    )


@admin.register(models.NumericAnswer)
class NumericAnswerAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'numeric',
        'sku',
    )
    readonly_fields = (
        'answer',
        'numeric',
    )

    def sku(self, instance):
        return instance.answer.question.sku


@admin.register(models.OptionAnswer)
class OptionAnswerAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'text',
    )
    readonly_fields = (
        'answer',
        'option',
    )

    def text(self, instance):
        return instance.option.option


@admin.register(models.ChoiceAnswer)
class ChoiceAnswerAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'choice',
    )
    readonly_fields = (
        'answer',
        'choice',
    )
