from django_filters import rest_framework as filters

from apps.market.models import Store


class StoreFilter(filters.FilterSet):
    class Meta:
        model = Store
        fields = [
            'retailer',
        ]
