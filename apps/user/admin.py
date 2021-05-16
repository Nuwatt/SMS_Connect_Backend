from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseModelAdmin
from apps.user import models

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'fullname', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': (
            'fullname',
            'contact_number',
            'avatar',
        )}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_agent_user', 'is_archived',
                'is_portal_user', 'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'fullname',
                'password1',
                'password2',
                'is_agent_user',
                'is_portal_user'
            ),
        }),
    )
    ordering = ('-date_joined',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_archived', 'groups')


@admin.register(models.AgentUser)
class AgentUserAdmin(BaseModelAdmin):
    pass


@admin.register(models.PortalUser)
class PortalUserAdmin(BaseModelAdmin):
    pass


@admin.register(models.Role)
class RoleAdmin(BaseModelAdmin):
    list_display = (
        'name',
    ) + BaseModelAdmin.list_display

    search_fields = (
        'name',
    ) + BaseModelAdmin.search_fields
