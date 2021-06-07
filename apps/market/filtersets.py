from django_filters import rest_framework as filters

from apps.market.models import Store


class StoreFilter(filters.FilterSet):
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
