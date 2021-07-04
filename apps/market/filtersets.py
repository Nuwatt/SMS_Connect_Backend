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

    class Meta:
        model = Store
        fields = [
            'retailer',
            'city'
        ]


class RetailerFilter(filters.FilterSet):
    city = filters.CharFilter(
        field_name='store__city',
        label='city'
    )
    channel = filters.CharFilter(
        field_name='channel',
        label='channel'
    )
