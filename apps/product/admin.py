from django.contrib import admin

from apps.product import models
from apps.core.admin import BaseModelAdmin


@admin.register(models.Brand)
class BrandAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'sku__country',
    )


@admin.register(models.Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'sku__country',
    )


@admin.register(models.SKU)
class SKUAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'country',
    )
