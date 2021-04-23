from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.terms_and_conditions import models


@admin.register(models.TermsAndConditions)
class TermsAndConditionsAdmin(BaseModelAdmin):
    pass
