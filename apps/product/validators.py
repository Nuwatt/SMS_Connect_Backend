from django.core.validators import _lazy_re_compile
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from apps.core.validators import WordValidator


@deconstructible
class SKUNameValidator(WordValidator):
    message = _('Enter a valid sku name.')
    regex_message = _('Accepted letters, digits and _,- ')
    regex = _lazy_re_compile(
        r'^[aA-zZ0-9\-\_]+$'
    )


@deconstructible
class CategoryNameValidator(WordValidator):
    message = _('Enter a valid category name.')
    regex_message = _('Accepted words with letters, digits')
    regex = _lazy_re_compile(
        r'^[aA-zZ0-9\-]+$'
    )


@deconstructible
class BrandNameValidator(WordValidator):
    message = _('Enter a valid product name.')
    regex_message = _('Accepted words with letters, digits')
    regex = _lazy_re_compile(
        r'^[aA-zZ0-9\s\-]+$'
    )


validate_sku_name = SKUNameValidator()
validate_category_name = CategoryNameValidator()
validate_brand_name = BrandNameValidator()
