from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class SKUNotFound(NotFound):
    default_detail = _('SKU not found.')


class BrandNotFound(NotFound):
    default_detail = _('Brand not found.')


class CategoryNotFound(NotFound):
    default_detail = _('Category not found.')
