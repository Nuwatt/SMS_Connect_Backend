from datetime import datetime

from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter, NameSearchFilter
from apps.snap.models import SnapSKU, SnapBrand, SnapCategory, SnapStore


class SnapCityFilter(NameSearchFilter):
    country = IdInFilter(
        field_name="country",
        lookup_expr='in',
        label='country'
    )


class SnapCountryFilter(NameSearchFilter):
    pass


class SnapPriceMonitorFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='country_id',
        label='country',
        lookup_expr='in'
    )
    city = IdInFilter(
        field_name='city_id',
        label='city',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='brand_id',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='date',
        label='date',
    )
    exact_date = filters.DateFilter(
        field_name='date',
        label='date'
    )
    channel = IdInFilter(
        field_name='channel_id',
        label='channel',
        lookup_expr='in'

    )
    category = IdInFilter(
        field_name='category_id',
        label='category',
        lookup_expr='in'
    )
    sku = IdInFilter(
        field_name='sku_id',
        label='sku',
        lookup_expr='in'
    )
    month = filters.CharFilter(
        method='filter_month',
        label='month'
    )

    def filter_month(self, queryset, name, value):
        dates = value.split(',')
        dates = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
        return queryset.filter(
            date__month__in=[date.month for date in dates],
            date__year__in=[date.year for date in dates]
        )


class SnapOutOfStockFilter(SnapPriceMonitorFilter):
    retailer = IdInFilter(
        field_name='retailer_id',
        label='retailer',
        lookup_expr='in'
    )
    store = IdInFilter(
        field_name='store_id',
        label='store',
        lookup_expr='in'
    )


class SnapDistributionFilter(SnapPriceMonitorFilter):
    pass


class SnapConsumerFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='city__country',
        label='country',
        lookup_expr='in'
    )
    city = IdInFilter(
        field_name='snap_city',
        label='snap_city',
        lookup_expr='in'
    )
    brand = IdInFilter(
        field_name='sku__brand',
        label='brand',
        lookup_expr='in'
    )
    date = filters.DateFromToRangeFilter(
        field_name='date',
        label='date',
    )
    exact_date = filters.DateFilter(
        field_name='date',
        label='date'
    )
    channel = IdInFilter(
        field_name='channel',
        label='channel',
        lookup_expr='in'

    )
    category = IdInFilter(
        field_name='sku__category',
        label='category',
        lookup_expr='in'
    )
    sku = IdInFilter(
        field_name='sku',
        label='sku',
        lookup_expr='in'
    )
    month = filters.CharFilter(
        method='filter_month',
        label='month'
    )

    def filter_month(self, queryset, name, value):
        dates = value.split(',')
        dates = [datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
        return queryset.filter(
            date__month__in=[date.month for date in dates],
            date__year__in=[date.year for date in dates]
        )


class SnapSKUFilter(filters.FilterSet):
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
        model = SnapSKU
        fields = [
            'brand',
            'category',
            'country',
        ]


class SnapBrandFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='snapsku__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )
    category = IdInFilter(
        field_name='snapsku__category',
        lookup_expr='in',
        label='category',
        distinct=True
    )

    class Meta:
        model = SnapBrand
        fields = [
            'country',
            'category',
        ]


class SnapCategoryFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='snapsku__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )

    class Meta:
        model = SnapCategory
        fields = [
            'country',
        ]


class SnapStoreFilter(filters.FilterSet):
    retailer = IdInFilter(
        field_name='retailer',
        lookup_expr='in',
        label='retailer'
    )
    city = IdInFilter(
        field_name='snap_city',
        lookup_expr='in',
        label='snap_city'
    )
    country = IdInFilter(
        field_name='city__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )

    class Meta:
        model = SnapStore
        fields = [
            'retailer',
            'snap_city',
            'country'
        ]


class SnapRetailerFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='store__city',
        lookup_expr='in',
        label='snap_city'
    )
    country = IdInFilter(
        field_name='snapstore__city__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )
