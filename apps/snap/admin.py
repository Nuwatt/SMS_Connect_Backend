from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.snap import models


@admin.register(models.PriceMonitorSnap)
class PriceMonitorSnapAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'sku',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'category',
        'brand',
        'channel',
        'city__country',
    )
