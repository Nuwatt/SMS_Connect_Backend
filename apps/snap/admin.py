from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.snap import models


@admin.register(models.PriceMonitorSnap)
class PriceMonitorSnapAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku',
        'date',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'sku__category',
        'sku__brand',
        'channel',
        'city__country',
        'city',
    )
    raw_id_fields = [
        'city',
        'channel',
        'sku',
    ]


@admin.register(models.OutOfStockSnap)
class OutOfStockSnapAdmin(BaseModelAdmin):
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
        'store',
    ]


@admin.register(models.DistributionSnap)
class DistributionSnapAdmin(BaseModelAdmin):
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
    ]


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
class SnapChannelAdmin(BaseModelAdmin):
    pass


@admin.register(models.SnapRetailer)
class SnapRetailerAdmin(BaseModelAdmin):
    pass


@admin.register(models.SnapStore)
class SnapStoreAdmin(BaseModelAdmin):
    pass


@admin.register(models.SnapCategory)
class SnapCategoryAdmin(BaseModelAdmin):
    pass


@admin.register(models.SnapBrand)
class SnapBrandAdmin(BaseModelAdmin):
    pass


@admin.register(models.SnapSKU)
class SnapSKUAdmin(BaseModelAdmin):
    pass
