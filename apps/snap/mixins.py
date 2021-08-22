from apps.snap.usecases.brand_usecases import GetSnapBrandUseCase
from apps.snap.usecases.category_usecases import GetSnapCategoryUseCase
from apps.snap.usecases.channel_usecases import GetSnapChannelUseCase
from apps.snap.usecases.price_monitor_usecases import GetPriceMonitorSnapUseCase
from apps.snap.usecases.out_of_stock_usecases import GetOutOfStockSnapUseCase
from apps.snap.usecases.distribution_usecases import GetDistributionSnapUseCase
from apps.snap.usecases.consumer_usecases import GetConsumerSnapUseCase
from apps.snap.usecases.retailer_usecases import GetSnapRetailerUseCase
from apps.snap.usecases.sku_usecases import GetSnapSKUUseCase
from apps.snap.usecases.store_usecases import GetSnapStoreUseCase


class PriceMonitorSnapMixin:
    def get_price_monitor_snap(self, *args, **kwargs):
        return GetPriceMonitorSnapUseCase(
            price_monitor_snap_id=self.kwargs.get('price_monitor_snap_id')
        ).execute()


class OutOfStockSnapMixin:
    def get_out_of_stock_snap(self, *args, **kwargs):
        return GetOutOfStockSnapUseCase(
            out_of_stock_snap_id=self.kwargs.get('out_of_stock_snap_id')
        ).execute()


class ConsumerSnapMixin:
    def get_consumer_snap(self, *args, **kwargs):
        return GetConsumerSnapUseCase(
            consumer_snap_id=self.kwargs.get('consumer_snap_id')
        ).execute()


class DistributionSnapMixin:
    def get_distribution_snap(self, *args, **kwargs):
        return GetDistributionSnapUseCase(
            distribution_snap_id=self.kwargs.get('distribution_snap_id')
        ).execute()


class SnapBrandMixin:
    def get_snap_brand(self, *args, **kwargs):
        return GetSnapBrandUseCase(
            snap_brand_id=self.kwargs.get('snap_brand_id')
        ).execute()


class SnapSKUMixin:
    def get_snap_sku(self, *args, **kwargs):
        return GetSnapSKUUseCase(
            snap_sku_id=self.kwargs.get('snap_sku_id')
        ).execute()


class SnapCategoryMixin:
    def get_snap_category(self, *args, **kwargs):
        return GetSnapCategoryUseCase(
            snap_category_id=self.kwargs.get('snap_category_id')
        ).execute()


class SnapStoreMixin:
    def get_snap_store(self, *args, **kwargs):
        return GetSnapStoreUseCase(
            snap_store_id=self.kwargs.get('snap_store_id')
        ).execute()


class SnapRetailerMixin:
    def get_snap_retailer(self, *args, **kwargs):
        return GetSnapRetailerUseCase(
            snap_retailer_id=self.kwargs.get('snap_retailer_id')
        ).execute()


class SnapChannelMixin:
    def get_snap_channel(self, *args, **kwargs):
        return GetSnapChannelUseCase(
            snap_channel_id=self.kwargs.get('snap_channel_id')
        ).execute()
