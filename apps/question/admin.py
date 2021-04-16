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
    pass


@admin.register(models.QuestionOption)
class QuestionOptionAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'option',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'option',
    )


@admin.register(models.QuestionType)
class QuestionOptionAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'type',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'type',
    )
