from django.conf import settings
from rest_framework.pagination import CursorPagination, LimitOffsetPagination
from rest_framework.response import Response


class CustomCursorPagination(CursorPagination):
    page_size_query_param = 'limit'


class ReportPagination(LimitOffsetPagination):
    default_limit = settings.REPORTING_MAX_LIMIT

    def get_paginated_response(self, data):
        return Response(data)


class SnapReportPagination(LimitOffsetPagination):
    default_limit = settings.SNAP_REPORTING_MAX_LIMIT

    def get_paginated_response(self, data):
        return Response(data)
