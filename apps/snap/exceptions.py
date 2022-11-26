from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound, ValidationError


class PriceMonitorSnapNotFound(NotFound):
    default_detail = _('Price monitor snap not found.')


class OutOfStockSnapNotFound(NotFound):
    default_detail = _('Out of Stock snap not found.')


class SnapConsumerNotFound(NotFound):
    default_detail = _('Consumer snap not found.')


class DistributionSnapNotFound(NotFound):
    default_detail = _('Distribution snap not found.')


class SnapCityNotFound(NotFound):
    default_detail = _('City not found.')


class SnapCountryNotFound(NotFound):
    default_detail = _('Country not found.')


class SnapCountryDuplicate(ValidationError):
    default_detail = _('Duplicate Snap Country exists. Please Check')


class SnapCityDuplicate(ValidationError):
    default_detail = _('Duplicate Snap City exists. Please Check')


class SnapChannelDuplicate(ValidationError):
    default_detail = _('Duplicate Snap Channel exists. Please Check')


class SnapCategoryDuplicate(ValidationError):
    default_detail = _('Duplicate Snap Category exists. Please Check')


class SnapBrandDuplicate(ValidationError):
    default_detail = _('Duplicate Snap Brand exists. Please Check')


class SnapSKUDuplicate(ValidationError):
    default_detail = _('Duplicate Snap SKU exists. Please Check')
