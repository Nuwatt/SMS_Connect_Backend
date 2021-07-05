from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter
from apps.market.models import Store


class StoreFilter(filters.FilterSet):
    retailer = IdInFilter(
        field_name='retailer',
        lookup_expr='in',
        label='retailer'
    )
    city = IdInFilter(
        field_name='city',
        lookup_expr='in',
        label='city'
    )
    country = IdInFilter(
        field_name='city__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )

    class Meta:
        model = Store
        fields = [
            'retailer',
            'city',
            'country'
        ]


class RetailerFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='store__city',
        lookup_expr='in',
        label='city'
    )
    country = IdInFilter(
        field_name='store__city__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )
