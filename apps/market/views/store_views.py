from apps.core import generics
from apps.market.filtersets import StoreFilter
from apps.market.mixins import StoreMixin
from apps.market.serializers import store_serializers
from apps.market.usecases import store_usecases


class AddStoreView(generics.CreateAPIView):
    """
    Use this end-point to add new store
    """
    serializer_class = store_serializers.AddStoreSerializer

    def perform_create(self, serializer):
        return store_usecases.AddStoreUseCase(
            serializer=serializer
        ).execute()


class ListStoreView(generics.ListAPIView):
    """
    Use this end-point to list all store
    """
    serializer_class = store_serializers.ListStoreSerializer
    filterset_class = StoreFilter

    def get_queryset(self):
        return store_usecases.ListStoreUseCase().execute()


class UpdateStoreView(generics.UpdateAPIView, StoreMixin):
    """
    Use this end-point to update specific store
    """
    serializer_class = store_serializers.UpdateStoreSerializer

    def get_object(self):
        return self.get_store()

    def perform_update(self, serializer):
        return store_usecases.UpdateStoreUseCase(
            serializer=serializer,
            store=self.get_object()
        ).execute()


class DeleteStoreView(generics.DestroyAPIView, StoreMixin):
    """
    Use this end-point to delete specific store
    """

    def get_object(self):
        return self.get_store()

    def perform_destroy(self, instance):
        return store_usecases.DeleteStoreUseCase(
            store=self.get_object()
        ).execute()
