from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.response import models


@admin.register(models.Response)
class ResponseAdmin(BaseModelAdmin):
    pass


@admin.register(models.Answer)
class AnswerAdmin(BaseModelAdmin):
    pass
