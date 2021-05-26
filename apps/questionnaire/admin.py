from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.questionnaire import models


@admin.register(models.QuestionnaireType)
class QuestionnaireTypeAdmin(BaseModelAdmin):
    list_display = (
                       'name',
                   ) + BaseModelAdmin.list_display

    search_fields = (
                        'name',
                    ) + BaseModelAdmin.search_fields


@admin.register(models.Questionnaire)
class QuestionnaireAdmin(BaseModelAdmin):
    raw_id_fields = (
        'city',
        'country',
        'tags'
    )
    list_display = (
                       'name',
                   ) + BaseModelAdmin.list_display

    search_fields = (
                        'name',
                    ) + BaseModelAdmin.search_fields

    list_filter = (
        'questionnaire_type',
        'is_archived',
    )
