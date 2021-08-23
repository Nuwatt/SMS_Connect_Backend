from django_filters import rest_framework as filters

from apps.core.filtersets import IdInFilter
from apps.snap.models import SnapSKU, SnapBrand, SnapCategory, SnapStore


class PriceMonitorSnapFilter(filters.FilterSet):
    country = IdInFilter(
        field_name='city__country',
        label='country',
        lookup_expr='in'
    )
    city = IdInFilter(
        field_name='city',
        label='city',
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


class OutOfStockSnapFilter(PriceMonitorSnapFilter):
    pass


class ConsumerSnapFilter(PriceMonitorSnapFilter):
    pass


class DistributionSnapFilter(PriceMonitorSnapFilter):
    pass



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

    class Meta:
        model = SnapBrand
        fields = [
            'country',
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
        field_name='city',
        lookup_expr='in',
        label='city'
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
            'city',
            'country'
        ]


class SnapRetailerFilter(filters.FilterSet):
    city = IdInFilter(
        field_name='store__city',
        lookup_expr='in',
        label='city'
    )
    country = IdInFilter(
        field_name='snapstore__city__country',
        lookup_expr='in',
        label='country',
        distinct=True
    )
