from django_filters import rest_framework as filters

from apps.response.models import Response


class ResponseFilter(filters.FilterSet):
    class Meta:
        model = Response
        fields = [
            'is_completed',
        ]
