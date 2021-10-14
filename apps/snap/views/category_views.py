from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from apps.core import generics
from apps.snap.filtersets import SnapCategoryFilter
from apps.snap.mixins import SnapCategoryMixin
from apps.snap.usecases import category_usecases
from apps.snap.serializers import category_serializers


class AddSnapCategoryView(generics.CreateAPIView):
    """
    Use this end-point to add new snap category
    """
    serializer_class = category_serializers.AddSnapCategorySerializer

    def perform_create(self, serializer):
        return category_usecases.AddSnapCategoryUseCase(
            serializer=serializer
        ).execute()


class ListSnapCategoryView(generics.ListAPIView):
    """
    Use this end-point to list all snap category
    """
    serializer_class = category_serializers.ListSnapCategorySerializer
    filterset_class = SnapCategoryFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name']

    def get_queryset(self):
        return category_usecases.ListSnapCategoryUseCase().execute()


class UpdateSnapCategoryView(generics.UpdateAPIView, SnapCategoryMixin):
    """
    Use this end-point to update specific snap category
    """
    serializer_class = category_serializers.UpdateSnapCategorySerializer

    def get_object(self):
        return self.get_snap_category()

    def perform_update(self, serializer):
        return category_usecases.UpdateSnapCategoryUseCase(
            serializer=serializer,
            snap_category=self.get_object()
        ).execute()


class DeleteSnapCategoryView(generics.DestroyAPIView, SnapCategoryMixin):
    """
    Use this end-point to delete specific snap category
    """

    def get_object(self):
        return self.get_snap_category()

    def perform_destroy(self, instance):
        return category_usecases.DeleteSnapCategoryUseCase(
            snap_category=self.get_object()
        ).execute()
