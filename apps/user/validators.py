from django.core.exceptions import ValidationError
from django.core.validators import _lazy_re_compile
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from apps.core.validators import Validator


@deconstructible
class DateOfBirthValidator(Validator):
    message = _('Enter a valid DOB.')
    min_year = 1930

    def __call__(self, value):
        if not value:
            raise ValidationError(self.message, code=self.code)

        now = timezone.now().year
        age = now - value.year

        if age < 10:
            raise ValidationError(_('Under age: 10 is not accepted.'), code=self.code)

        if age > 90:
            raise ValidationError(_('Above age: 90 is not accepted.'), code=self.code)


validate_date_of_birth = DateOfBirthValidator()
