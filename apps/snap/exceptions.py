from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class PriceMonitorSnapNotFound(NotFound):
    default_detail = _('Price monitor snap not found.')


class OutOfStockSnapNotFound(NotFound):
    default_detail = _('Out of Stock snap not found.')


class ConsumerSnapNotFound(NotFound):
    default_detail = _('Consumer snap not found.')


class DistributionSnapNotFound(NotFound):
    default_detail = _('Distribution snap not found.')


class SnapCityNotFound(NotFound):
    default_detail = _('City not found.')


class SnapCountryNotFound(NotFound):
    default_detail = _('Country not found.')
