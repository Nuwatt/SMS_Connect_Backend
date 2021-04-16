from apps.market.usecases.store_usecases import GetStoreUseCase
from apps.market.usecases.retailer_usecases import GetRetailerUseCase


class StoreMixin:
    def get_store(self, *args, **kwargs):
        return GetStoreUseCase(
            store_id=self.kwargs.get('store_id')
        ).execute()


class RetailerMixin:
    def get_retailer(self, *args, **kwargs):
        return GetRetailerUseCase(
            retailer_id=self.kwargs.get('retailer_id')
        ).execute()
