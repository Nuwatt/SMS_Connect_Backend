from django.conf import settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class ReportPagination(LimitOffsetPagination):
    default_limit = settings.REPORTING_MAX_LIMIT

    def get_paginated_response(self, data):
        return Response(data)
