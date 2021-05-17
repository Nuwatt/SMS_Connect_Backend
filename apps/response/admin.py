from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.response import models


@admin.register(models.Response)
class ResponseAdmin(BaseModelAdmin):
    pass


@admin.register(models.Answer)
class AnswerAdmin(BaseModelAdmin):
    pass


@admin.register(models.ImageAnswer)
class ImageAnswerAdmin(BaseModelAdmin):
    pass


@admin.register(models.InputAnswer)
class InputAnswerAdmin(BaseModelAdmin):
    pass


@admin.register(models.OptionAnswer)
class OptionAnswerAdmin(BaseModelAdmin):
    pass


@admin.register(models.ChoiceAnswer)
class ChoiceAnswerAdmin(BaseModelAdmin):
    pass
