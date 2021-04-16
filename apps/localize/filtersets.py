from django_filters import rest_framework as filters

from apps.localize.models import Area, City


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
