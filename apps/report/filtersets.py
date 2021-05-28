from django_filters import rest_framework as filters


class SKUMinMaxFilter(filters.FilterSet):
    city = filters.CharFilter(
        field_name='answer__response__retailer__city',
        label='city'
    )
    retailer = filters.CharFilter(
        field_name='answer__response__retailer',
        label='retailer'
    )
    sku = filters.CharFilter(
        field_name='answer__question__sku',
        label='sku'
    )
    from_date = filters.DateFilter(
        field_name='answer__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='answer__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )
