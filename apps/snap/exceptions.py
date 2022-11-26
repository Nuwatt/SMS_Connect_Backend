from django.utils.translation import gettext_lazy as _
from rest_framework import status

from rest_framework.exceptions import NotFound, APIException


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


class SnapDuplicate(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'invalid'


class SnapCountryDuplicate(SnapDuplicate):
    default_detail = _('Duplicate Snap Country exists. Please Check')


class SnapCityDuplicate(SnapDuplicate):
    default_detail = _('Duplicate Snap City exists. Please Check')


class SnapChannelDuplicate(SnapDuplicate):
    default_detail = _('Duplicate Snap Channel exists. Please Check')


class SnapCategoryDuplicate(SnapDuplicate):
    default_detail = _('Duplicate Snap Category exists. Please Check')


class SnapBrandDuplicate(SnapDuplicate):
    default_detail = _('Duplicate Snap Brand exists. Please Check')


class SnapSKUDuplicate(SnapDuplicate):
    default_detail = _('Duplicate Snap SKU exists. Please Check')
