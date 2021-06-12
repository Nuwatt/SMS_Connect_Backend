from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter
from apps.product.models import SKU, Brand


class SKUFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='brand__category'
    )

    brand = IdInFilter(
        field_name='brand',
        lookup_expr='in',
        label='brand'
    )

    class Meta:
        model = SKU
        fields = [
            'brand',
            'category',
        ]


class BrandFilter(filters.FilterSet):
    class Meta:
        model = Brand
        fields = [
            'category',
        ]
