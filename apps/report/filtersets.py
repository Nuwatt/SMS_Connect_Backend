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
    city = filters.CharFilter(
        field_name='id',
        label='city'
    )


class AnswerPerCountryFilter(AnswerFilter):
    country = filters.CharFilter(
        field_name='id',
        label='country'
    )


class AnswerPerSKUFilter(AnswerFilter):
    sku = filters.CharFilter(
        field_name='id',
        label='sku'
    )
