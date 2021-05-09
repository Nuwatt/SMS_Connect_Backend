from apps.core import generics
from apps.market.mixins import RetailerMixin
from apps.market.serializers import retailer_serializers
from apps.market.usecases import retailer_usecases


class AddRetailerView(generics.CreateAPIView):
    """
    Use this end-point to add new retailer
    """
    serializer_class = retailer_serializers.AddRetailerSerializer

    def perform_create(self, serializer):
        return retailer_usecases.AddRetailerUseCase(
            serializer=serializer
        ).execute()


class ListRetailerView(generics.ListAPIView):
    """
    Use this end-point to list all retailer
    """
    serializer_class = retailer_serializers.ListRetailerSerializer

    def get_queryset(self):
        return retailer_usecases.ListRetailerUseCase().execute()


class UpdateRetailerView(generics.UpdateAPIView, RetailerMixin):
    """
    Use this end-point to update specific retailer
    """
    serializer_class = retailer_serializers.UpdateRetailerSerializer

    def get_object(self):
        return self.get_retailer()

    def perform_update(self, serializer):
        return retailer_usecases.UpdateRetailerUseCase(
            serializer=serializer,
            retailer=self.get_object()
        ).execute()


class DeleteRetailerView(generics.DestroyAPIView, RetailerMixin):
    """
    Use this end-point to delete specific retailer
    """

    def get_object(self):
        return self.get_retailer()

    def perform_destroy(self, instance):
        return retailer_usecases.DeleteRetailerUseCase(
            retailer=self.get_object()
        ).execute()
