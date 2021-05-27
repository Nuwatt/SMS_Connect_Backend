from django.core.exceptions import ValidationError
from django.core.validators import _lazy_re_compile
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class Validator:
    message = None
    code = 'invalid'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        raise NotImplementedError("Subclasses should implement this!")

    def __eq__(self, other):
        return (
                isinstance(other, Validator) and
                (self.message == other.message) and
                (self.code == other.code)
        )


@deconstructible
class WordValidator(Validator):
    regex_message = None
    regex = None

    def __call__(self, value):
        """
        raise on:
        1. empty value
        2. not matched to regex
        """
        if not value:
            raise ValidationError(self.message, code=self.code)

        if not self.regex.match(value):
            raise ValidationError(self.regex_message, code=self.code)


@deconstructible
class PhoneNumberValidator(Validator):
    message = _('Enter a valid phone number.')
    phone_number_regex = _lazy_re_compile(r'^[0-9/+/-]+$')

    def __call__(self, value):
        if not value:
            raise ValidationError(self.message, code=self.code)

        if not self.phone_number_regex.match(value):
            raise ValidationError(self.message, code=self.code)


@deconstructible
class LatitudeValidator(Validator):
    message = _('Enter a valid latitude.')

    def __call__(self, value):
        if not value:
            raise ValidationError(self.message, code=self.code)
        if not (-90 <= value <= 90):
            raise ValidationError(self.message, code=self.code)


@deconstructible
class LongitudeValidator(Validator):
    message = _('Enter a valid longitude.')

    def __call__(self, value):
        if not value:
            raise ValidationError(self.message, code=self.code)

        if not (-180 <= value <= 180):
            raise ValidationError(self.message, code=self.code)


@deconstructible
class CSVFileValidator(Validator):
    message = _('Provided file is not a csv file.')

    def __call__(self, value):
        if not value:
            raise ValidationError(_('This field is required.'), code=self.code)

        if value.content_type != 'text/csv':
            raise ValidationError(self.message, code=self.code)


@deconstructible
class ImageValidator(Validator):
    message = _('The maximum image file size that can be uploaded is 4MB')
    file_size = 4194304

    def __call__(self, value):
        if not value:
            raise ValidationError(self.message, code=self.code)

        if value.size > self.file_size:
            raise ValidationError(self.message, code=self.code)


validate_phone_number = PhoneNumberValidator()
validate_latitude = LatitudeValidator()
validate_longitude = LongitudeValidator()
validate_csv_file = CSVFileValidator()
validate_image = ImageValidator()
