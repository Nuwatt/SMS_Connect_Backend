from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class CityNotFound(NotFound):
    default_detail = _('City not found.')


class CountryNotFound(NotFound):
    default_detail = _('Country not found.')


class AreaNotFound(NotFound):
    default_detail = _('Area not found.')


class NationalityNotFound(NotFound):
    default_detail = _('Nationality not found.')

class RegionNotFound(NotFound):
    default_detail = _('Region not found.')
