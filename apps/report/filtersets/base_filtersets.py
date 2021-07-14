from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter


class ResponseFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='store__city__country',
        label='country',
        lookup_expr='in'
    )
    city = IdInFilter(
        field_name='store__city',
        label='city',
        lookup_expr='in'
    )
    sku = IdInFilter(
        field_name='answer__question__sku',
        label='sku',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='answer__question__sku__brand',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='completed_at__date',
        label='date'
    )
    exact_date = filters.DateFilter(
        field_name='completed_at__date',
        label='date'
    )
    store = IdInFilter(
        field_name='store',
        label='store',
        lookup_expr='in'

    )
    channel = IdInFilter(
        field_name='store__channel',
        label='channel',
        lookup_expr='in'

    )
    retailer = IdInFilter(
        field_name='store__retailer',
        label='store',
        lookup_expr='in'

    )


class SKUResponseFilter(ResponseFilter):
    sku = IdInFilter(
        field_name='sku',
        label='sku',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )


class BrandResponseFilter(ResponseFilter):
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )


class NumericAnswerReportFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='answer__response__store__city__country',
        label='country',
        lookup_expr='in'
    )
    city = IdInFilter(
        field_name='answer__response__store__city',
        label='city',
        lookup_expr='in'
    )
    sku = IdInFilter(
        field_name='answer__question__sku',
        label='sku',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='answer__question__sku__brand',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='answer__response__completed_at__date',
        label='date'
    )
    exact_date = filters.DateFilter(
        field_name='answer__response__completed_at__date',
        label='date'
    )
    store = IdInFilter(
        field_name='answer__response__store',
        label='store',
        lookup_expr='in'

    )
    channel = IdInFilter(
        field_name='answer__response__store__channel',
        label='channel',
        lookup_expr='in'

    )
    retailer = IdInFilter(
        field_name='answer__response__store__retailer',
        label='store',
        lookup_expr='in'

    )
