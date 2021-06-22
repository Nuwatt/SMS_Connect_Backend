from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter


class SKUMinMaxReportFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='question__answer__response__store__city',
        label='city',
        lookup_expr='in'
    )
    country = IdInFilter(
        field_name='question__answer__response__store__city__country',
        label='country',
        lookup_expr='in'
    )
    store = IdInFilter(
        field_name='question__answer__response__store',
        label='store',
        lookup_expr='in'

    )
    sku = IdInFilter(
        field_name='id',
        label='sku',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='question__answer__response__completed_at__date',
        label='date'
    )
    exact_date = filters.DateFilter(
        field_name='question__answer__response__completed_at__date',
        label='date'
    )
    # from_date = filters.DateFilter(
    #     field_name='question__answer__response__completed_at__date',
    #     label='from date',
    #     lookup_expr='gte'
    # )
    # till_date = filters.DateFilter(
    #     field_name='question__answer__response__completed_at__date',
    #     label='till date',
    #     lookup_expr='lte'
    # )


class SKUReportFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='question__answer__response__store__city',
        label='city',
        lookup_expr='in'
    )
    country = IdInFilter(
        field_name='country',
        label='country',
        lookup_expr='in'
    )
    store = IdInFilter(
        field_name='question__answer__response__store',
        label='store',
        lookup_expr='in'

    )
    sku = IdInFilter(
        field_name='id',
        label='sku',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='brand',
        label='brand',
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
    sku = IdInFilter(
        field_name='store__response__answer__question__sku',
        label='sku',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='store__response__completed_at__date',
        label='date'
    )
    exact_date = filters.DateFilter(
        field_name='store__response__completed_at__date',
        label='date'
    )
    store = IdInFilter(
        field_name='store',
        label='store',
        lookup_expr='in'

    )


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
    retailer = IdInFilter(
        field_name='store__retailer',
        label='store',
        lookup_expr='in'

    )


class AnswerPerCountryFilter(ResponseFilter):
    pass


class AnswerPerCityReportFilter(ResponseFilter):
    pass


class AnswerPerSKUFilter(SKUMinMaxReportFilter):
    pass


class BrandMinMaxReportFilter(ResponseFilter):
    brand = IdInFilter(
        field_name='brand',
        label='brand',
        lookup_expr='in'
    )


class TotalVisitFilter(AnswerFilter):
    city = IdInFilter(
        field_name='id',
        label='city',
        lookup_expr='in'
    )


class SKUCountryReportFilter(ResponseFilter):
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


class SKUMonthReportFilter(ResponseFilter):
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


class AnswerPerCountryReportFilter(ResponseFilter):
    pass


class AnswerPerSKUReportFilter(ResponseFilter):
    pass
