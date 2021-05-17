from django_filters import rest_framework as filters


class NameSearchFilter(filters.FilterSet):
    search = filters.CharFilter(
        method='search_name',
        label='search'
    )

    def search_name(self, queryset, name, value):
        return queryset.filter(
            name__icontains=value
        )


