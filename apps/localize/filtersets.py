from django_filters import rest_framework as filters

from apps.localize.models import Area, City, Country, Region


class AreaFilter(filters.FilterSet):
    class Meta:
        model = Area
        fields = [
            'country',
            'city',
        ]


class CityFilter(filters.FilterSet):
    class Meta:
        model = City
        fields = [
            'country',
        ]

class CountryFilter(filters.FilterSet):
    class Meta:
        model = Country
        fields = [
            'region',
        ]
