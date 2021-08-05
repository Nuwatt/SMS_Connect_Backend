from apps.snap.usecases.price_monitor_usecases import GetPriceMonitorSnapUseCase
from apps.snap.usecases.out_of_stock_usecases import GetOutOfStockSnapUseCase
from apps.snap.usecases.consumer_usecases import GetConsumerSnapUseCase


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

