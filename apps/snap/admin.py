from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.snap import models


@admin.register(models.PriceMonitorSnap)
class PriceMonitorSnapAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'sku__category',
        'sku__brand',
        'channel',
        'city__country',
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
