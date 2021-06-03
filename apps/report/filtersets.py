from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter


class SKUMinMaxFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='answer__response__store__city',
        label='city',
        lookup_expr='in'
    )
    store = IdInFilter(
        field_name='answer__response__store',
        label='retailer',
        lookup_expr='in'

    )
    sku = IdInFilter(
        field_name='answer__question__sku',
        label='sku',
        lookup_expr='in'
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


class SKUReportFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='question__answer__response__store__city',
        label='city',
        lookup_expr='in'
    )
    store = IdInFilter(
        field_name='question__answer__response__store',
        label='retailer',
        lookup_expr='in'

    )
    sku = IdInFilter(
        field_name='id',
        label='sku',
        lookup_expr='in'
    )
    from_date = filters.DateFilter(
        field_name='question__answer__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='question__answer__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )


class AnswerFilter(filters.FilterSet):
    sku = filters.CharFilter(
        field_name='retailer__response__answer__question__sku',
        label='sku'
    )
    from_date = filters.DateFilter(
        field_name='retailer__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='retailer__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )


class AnswerPerCityFilter(AnswerFilter):
    city = IdInFilter(
        field_name='id',
        label='city',
        lookup_expr='in'
    )


class AnswerPerCountryFilter(AnswerFilter):
    country = IdInFilter(
        field_name='id',
        label='country',
        lookup_expr='in'

    )


class AnswerPerSKUFilter(AnswerFilter):
    sku = IdInFilter(
        field_name='id',
        label='sku',
        lookup_expr='in'
    )
