from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.question import models


@admin.register(models.QuestionStatement)
class QuestionStatementAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'statement',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'statement',
    )


@admin.register(models.Question)
class QuestionAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'statement',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'statement',
    )
    raw_id_fields = (
        'brand',
        'questionnaire',
        'sku'
    )
    list_filter = (
        'question_type',
    )


@admin.register(models.QuestionOption)
class QuestionOptionAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'option',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'option',
    )
    raw_id_fields = (
        'question',
    )


@admin.register(models.QuestionType)
class QuestionTypeAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )


@admin.register(models.QuestionTypeChoice)
class QuestionTypeChoiceAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'question_type',
        'choice',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'choice',
    )
    list_filter = (
        'question_type',
    )
