from django.db.models import Q
from django_filters import rest_framework as filters

from apps.user.models import AgentUser, PortalUser


class AgentUserFilter(filters.FilterSet):
    search = filters.CharFilter(
        method='search_user',
        label='search'
    )

    class Meta:
        model = AgentUser
        fields = [
            'search',
        ]

    def search_user(self, queryset, name, value):
        return queryset.filter(
            Q(id__icontains=value) |
            Q(user__fullname__icontains=value) |
            Q(user__nationality__name__icontains=value) |
            Q(user__email__icontains=value) |
            Q(user__email__icontains=value) |
            Q(operation_country__name__icontains=value) |
            Q(operation_city__name__icontains=value) |
            Q(user__username__icontains=value)
        )


class PortalUserFilter(filters.FilterSet):
    search = filters.CharFilter(
        method='search_user',
        label='search'
    )

    class Meta:
        model = PortalUser
        fields = [
            'search',
        ]

    def search_user(self, queryset, name, value):
        return queryset.filter(
            Q(id__icontains=value) |
            Q(user__fullname__icontains=value) |
            Q(user__nationality__name__icontains=value) |
            Q(user__email__icontains=value) |
            Q(role__name__icontains=value) |
            Q(position__icontains=value) |
            Q(user__username__icontains=value)
        )
