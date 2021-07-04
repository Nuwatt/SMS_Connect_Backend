from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics, status
from rest_framework.response import Response

from apps.core.exceptions import NoContent
from apps.core.mixins import LoggingErrorsMixin
from apps.core.serializers import MessageResponseSerializer
from apps.user.permissions import IsAdminPortalUser


class GenericAPIView(generics.GenericAPIView):
    logging_methods = ['GET']


class CreateAPIView(LoggingErrorsMixin, generics.CreateAPIView):
    logging_methods = ['POST']
    permission_classes = (IsAdminPortalUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = self.perform_create(serializer)
        return self.response(
            result=result,
            serializer=serializer,
            status_code=status.HTTP_201_CREATED
        )

    def response(self, result, serializer, status_code):
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status_code, headers=headers)


class CreateWithMessageAPIView(CreateAPIView):
    message = _('Performed Successfully.')

    def response(self, result, serializer, status_code):
        return Response(
            {
                'message': self.message
            }, status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={200: MessageResponseSerializer()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(LoggingErrorsMixin, generics.ListAPIView):
    logging_methods = ['GET']

    no_content_error_message = _('No Content At The Moment.')

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        if len(queryset) > 0:
            return self.custom_queryset(queryset)
        raise NoContent(self.no_content_error_message)

    def custom_queryset(self, queryset):
        return queryset


class UpdateAPIView(LoggingErrorsMixin, generics.UpdateAPIView):
    logging_methods = ['PUT', 'PATCH']
    permission_classes = (IsAdminPortalUser,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return self.response(serializer=serializer)

    def response(self, serializer):
        return Response(serializer.data)


class DestroyAPIView(LoggingErrorsMixin, generics.DestroyAPIView):
    logging_methods = ['DELETE']
    permission_classes = (IsAdminPortalUser,)


class RetrieveAPIView(LoggingErrorsMixin, generics.RetrieveAPIView):
    logging_methods = ['GET']

