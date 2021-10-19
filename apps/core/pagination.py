from django.conf import settings
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class CustomCursorPagination(CursorPagination):
    page_size_query_param = 'limit'


class ReportPagination(CustomCursorPagination):
    page_size = settings.REPORTING_MAX_LIMIT

    def get_paginated_response(self, data):
        return Response(data)
