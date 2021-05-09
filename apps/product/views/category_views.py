from apps.core import generics
from apps.product.mixins import CategoryMixin
from apps.product.serializers import category_serializers
from apps.product.usecases import category_usecases


class AddCategoryView(generics.CreateAPIView):
    """
    Use this end-point to add new category
    """
    serializer_class = category_serializers.AddCategorySerializer

    def perform_create(self, serializer):
        return category_usecases.AddCategoryUseCase(
            serializer=serializer
        ).execute()


class ListCategoryView(generics.ListAPIView):
    """
    Use this end-point to list all category
    """
    serializer_class = category_serializers.ListCategorySerializer

    def get_queryset(self):
        return category_usecases.ListCategoryUseCase().execute()


class UpdateCategoryView(generics.UpdateAPIView, CategoryMixin):
    """
    Use this end-point to update specific category
    """
    serializer_class = category_serializers.UpdateCategorySerializer

    def get_object(self):
        return self.get_category()

    def perform_update(self, serializer):
        return category_usecases.UpdateCategoryUseCase(
            serializer=serializer,
            category=self.get_object()
        ).execute()


class DeleteCategoryView(generics.DestroyAPIView, CategoryMixin):
    """
    Use this end-point to delete specific category
    """

    def get_object(self):
        return self.get_category()

    def perform_destroy(self, instance):
        return category_usecases.DeleteCategoryUseCase(
            category=self.get_object()
        ).execute()
