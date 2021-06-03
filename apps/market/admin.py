from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.market import models


@admin.register(models.Retailer)
class RetailerAdmin(BaseModelAdmin):
    list_display = (
        'name',
    ) + BaseModelAdmin.list_display

    search_fields = (
        'name',
    ) + BaseModelAdmin.search_fields


@admin.register(models.Store)
class StoreAdmin(BaseModelAdmin):
    list_display = (
        'name',
    ) + BaseModelAdmin.list_display

    search_fields = (
        'name',
    ) + BaseModelAdmin.search_fields

    raw_id_fields = (
        'city',
        'retailer'
    )


@admin.register(models.Channel)
class ChannelAdmin(BaseModelAdmin):
    list_display = (
        'name',
    ) + BaseModelAdmin.list_display

    search_fields = (
        'name',
    ) + BaseModelAdmin.search_fields
