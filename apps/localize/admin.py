from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.localize import models


class LocalizeModelAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )


@admin.register(models.Country)
class CountryAdmin(LocalizeModelAdmin):
    pass


@admin.register(models.City)
class CityAdmin(LocalizeModelAdmin):
    list_filter = (
        'country',
    )


@admin.register(models.Area)
class AreaAdmin(LocalizeModelAdmin):
    list_filter = (
        'country',
    )
