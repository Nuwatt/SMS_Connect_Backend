from django.core.exceptions import ValidationError as DjangoValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.core.models import BaseModel


class TermsAndConditions(BaseModel):
    text = models.TextField()

    def __str__(self):
        return str(self.id)

    def clean(self):
        # 1. there can be only one terms and conditions
        if TermsAndConditions.objects.unarchived().count() > 0:
            raise DjangoValidationError(_('Only one record is allowed.'))
