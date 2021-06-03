from django_filters import rest_framework as filters

from apps.product.models import SKU


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
