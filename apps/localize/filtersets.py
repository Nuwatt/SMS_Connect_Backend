from django_filters import rest_framework as filters

from apps.core.filtersets import NameSearchFilter
from apps.localize.models import Area, City, Country, Region


class AreaFilter(filters.FilterSet):
    class Meta:
        model = Area
        fields = [
            'country',
            'city',
        ]


class CityFilter(NameSearchFilter):
    class Meta:
        model = City
        fields = [
            'country',
            'search'
        ]


class CountryFilter(NameSearchFilter):
    class Meta:
        model = Country
        fields = [
            'region',
            'search'
        ]
