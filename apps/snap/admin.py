from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.snap import models


class SnapModelAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )


@admin.register(models.SnapCountry)
class SnapCountryAdmin(SnapModelAdmin):
    pass


@admin.register(models.SnapCity)
class SnapCityAdmin(SnapModelAdmin):
    list_filter = SnapModelAdmin.list_filter + (
        'country',
    )
    raw_id_fields = (
        'country',
    )


@admin.register(models.ConsumerSnap)
class ConsumerSnapAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'sku__category',
        'sku__brand',
        'city__country',
    )
    raw_id_fields = [
        'city',
        'sku',
        'channel'
    ]


@admin.register(models.SnapChannel)
class SnapChannelAdmin(SnapModelAdmin):
    pass


@admin.register(models.SnapRetailer)
class SnapRetailerAdmin(SnapModelAdmin):
    pass


@admin.register(models.SnapStore)
class SnapStoreAdmin(SnapModelAdmin):
    pass


@admin.register(models.SnapCategory)
class SnapCategoryAdmin(SnapModelAdmin):
    pass


@admin.register(models.SnapBrand)
class SnapBrandAdmin(SnapModelAdmin):
    pass


@admin.register(models.SnapSKU)
class SnapSKUAdmin(SnapModelAdmin):
    pass


# -------------new models----------

@admin.register(models.SnapPriceMonitor)
class SnapPriceMonitorAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku_name',
        'date',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'category_name',
        'brand_name',
        'channel_name',
        'country_name',
        'city_name',
    )


@admin.register(models.SnapOutOfStock)
class SnapOutOfStockAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku_name',
        'date',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'category_name',
        'brand_name',
        'channel_name',
        'country_name',
        'city_name',
    )


@admin.register(models.SnapDistribution)
class SnapDistributionAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku_name',
        'date',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'category_name',
        'brand_name',
        'channel_name',
        'country_name',
        'city_name',
    )
