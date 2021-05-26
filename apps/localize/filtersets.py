from django_filters import rest_framework as filters

from apps.core.filtersets import NameSearchFilter, IdInFilter
from apps.localize.models import Area, City, Country, Region


class AreaFilter(filters.FilterSet):
    class Meta:
        model = Area
        fields = [
            'country',
            'city',
        ]


class CityFilter(NameSearchFilter):
    questionnaire = filters.CharFilter(
        label='questionnaire',
        field_name='questionnaire__id',
    )
    country = IdInFilter(
        field_name="country",
        lookup_expr='in',
        label='country'
    )

    class Meta:
        model = City
        fields = [
            'country',
            'search',
            'questionnaire'
        ]


class CountryFilter(NameSearchFilter):
    questionnaire = filters.CharFilter(
        label='questionnaire',
        field_name='questionnaire__id',
    )

    class Meta:
        model = Country
        fields = [
            'region',
            'questionnaire',
            'search'
        ]
