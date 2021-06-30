from django.contrib.admin import ModelAdmin


class ArchiveMixin:
    def archive(self, request, queryset):
        queryset.archive()

    def restore(self, request, queryset):
        queryset.restore()

    archive.short_description = 'Archive selected items'
    restore.short_description = 'Restore selected items'


class BaseModelAdmin(ModelAdmin, ArchiveMixin):
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

    actions = [
        'archive',
        'restore',
    ]
