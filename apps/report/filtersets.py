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


class SKUMonthReportFilter(SKUMinMaxReportFilter):
    pass


class SKUCountryReportFilter(SKUMinMaxReportFilter):
    country = IdInFilter(
        field_name='country_id',
        label='country',
        lookup_expr='in'
    )


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
    from_date = filters.DateFilter(
        field_name='store__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='store__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )
    store = IdInFilter(
        field_name='store',
        label='store',
        lookup_expr='in'

    )


class AnswerPerCityFilter(filters.FilterSet):
    # sku = IdInFilter(
    #     field_name='store__response__answer__question__sku',
    #     label='sku',
    #     lookup_expr='in'
    # )
    city = IdInFilter(
        field_name='id',
        label='city',
        lookup_expr='in'
    )
    country = IdInFilter(
        field_name='country',
        label='country',
        lookup_expr='in'
    )
    from_date = filters.DateFilter(
        field_name='store__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='store__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )
    store = IdInFilter(
        field_name='store',
        label='store',
        lookup_expr='in'

    )


class AnswerPerCountryFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='id',
        label='country',
        lookup_expr='in'
    )

    # sku = IdInFilter(
    #     field_name='city__store__response__answer__question__sku',
    #     label='sku',
    #     lookup_expr='in'
    # )
    from_date = filters.DateFilter(
        field_name='city__store__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='city__store__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )
    store = IdInFilter(
        field_name='city__store',
        label='store',
        lookup_expr='in'

    )


class AnswerPerSKUFilter(SKUMinMaxReportFilter):
    pass


class BrandMinMaxReportFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='sku__question__answer__response__store__city',
        label='city',
        lookup_expr='in'
    )
    country = IdInFilter(
        field_name='sku__question__answer__response__store__city__country',
        label='country',
        lookup_expr='in'
    )
    store = IdInFilter(
        field_name='question__answer__response__store',
        label='store',
        lookup_expr='in'

    )
    sku = IdInFilter(
        field_name='sku',
        label='sku',
        lookup_expr='in'
    )
    from_date = filters.DateFilter(
        field_name='sku__question__answer__response__completed_at__date',
        label='from date',
        lookup_expr='gte'
    )
    till_date = filters.DateFilter(
        field_name='sku__question__answer__response__completed_at__date',
        label='till date',
        lookup_expr='lte'
    )


class TotalVisitFilter(AnswerFilter):
    city = IdInFilter(
        field_name='id',
        label='city',
        lookup_expr='in'
    )
