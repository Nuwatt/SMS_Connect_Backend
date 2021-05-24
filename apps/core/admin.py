from django.contrib.admin import ModelAdmin


class BaseModelAdmin(ModelAdmin):
    list_display = (
        'id',
        'updated',
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'id',
    )
    ordering = (
        '-created',
    )
    list_per_page = (
        25
    )
    readonly_fields = (
        'id',
        'created',
        'updated',
    )
    list_filter = ('is_archived',)

