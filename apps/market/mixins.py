from apps.market.usecases.store_usecases import GetStoreUseCase
from apps.market.usecases.retailer_usecases import GetRetailerUseCase
from apps.market.usecases.channel_usecases import GetChannelUseCase


class StoreMixin:
    def get_store(self, *args, **kwargs):
        return GetChannelUseCase(
            channel_id=self.kwargs.get('store_id')
        ).execute()


class RetailerMixin:
    def get_retailer(self, *args, **kwargs):
        return GetRetailerUseCase(
            retailer_id=self.kwargs.get('retailer_id')
        ).execute()


class ChannelMixin:
    def get_channel(self, *args, **kwargs):
        return GetChannelUseCase(
            channel_id=self.kwargs.get('channel_id')
        ).execute()
