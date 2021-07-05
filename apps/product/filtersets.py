from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter
from apps.product.models import SKU, Brand, Category


class SKUFilter(filters.FilterSet):
    category = IdInFilter(
        field_name='category',
        lookup_expr='in',
        label='category'
    )
    brand = IdInFilter(
        field_name='brand',
        lookup_expr='in',
        label='brand'
    )
    country = IdInFilter(
        field_name='country',
        lookup_expr='in',
        label='country'
    )

    class Meta:
        model = SKU
        fields = [
            'brand',
            'category',
            'country',
        ]


class BrandFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='sku__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )

    class Meta:
        model = Brand
        fields = [
            'country',
        ]


class CategoryFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='sku__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )

    class Meta:
        model = Category
        fields = [
            'country',
        ]
