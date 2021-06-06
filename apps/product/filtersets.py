from django_filters import rest_framework as filters

from apps.product.models import SKU, Brand


class SKUFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='brand__category'
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
