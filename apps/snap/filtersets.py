from django_filters import rest_framework as filters
from django_filters.widgets import RangeWidget

from apps.core.filtersets import IdInFilter


class PriceMonitorSnapFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='city__country',
        label='country',
        lookup_expr='in'
    )
    city = IdInFilter(
        field_name='city',
        label='city',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='date',
        label='date',
        widget=RangeWidget(attrs={'type': 'date'})
    )
    exact_date = filters.DateFilter(
        field_name='date',
        label='date'
    )
    channel = IdInFilter(
        field_name='channel',
        label='channel',
        lookup_expr='in'

    )
    category = IdInFilter(
        field_name='category',
        label='category',
        lookup_expr='in'
    )
