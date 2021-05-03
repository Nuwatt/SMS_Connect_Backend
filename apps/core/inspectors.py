from collections import OrderedDict

from drf_yasg import openapi
from drf_yasg.inspectors import DjangoRestResponsePagination
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination, CursorPagination


class CustomDjangoRestResponsePagination(DjangoRestResponsePagination):
    def get_paginated_response(self, paginator, response_schema):
        assert response_schema.type == openapi.TYPE_ARRAY, "array return expected for paged response"
        paged_schema = None
        if isinstance(paginator, (LimitOffsetPagination, PageNumberPagination, CursorPagination)):
            has_count = not isinstance(paginator, CursorPagination)
            pagination_response_schema = openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=OrderedDict((
                    ('count', openapi.Schema(type=openapi.TYPE_INTEGER) if has_count else None),
                    ('next', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('previous', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                    ('results', response_schema),
                )),
                required=['results']
            )
            paged_schema = openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=OrderedDict((
                    ('status', openapi.Schema(type=openapi.TYPE_BOOLEAN)),
                    ('error_message', openapi.Schema(type=openapi.TYPE_STRING, x_nullable=True)),
                    ('data', pagination_response_schema)
                )),
                required=['data']
            )

            if has_count:
                pagination_response_schema.required.insert(0, 'count')

        return paged_schema
