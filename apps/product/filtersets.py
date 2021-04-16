from django_filters import rest_framework as filters

from apps.product.models import SKU


class SKUFilter(filters.FilterSet):
    class Meta:
        model = SKU
        fields = [
            'brand',
            'category',
        ]
