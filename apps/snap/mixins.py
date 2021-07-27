from apps.snap.usecases.price_monitor_usecases import GetPriceMonitorSnapUseCase


class PriceMonitorSnapMixin:
    def get_price_monitor_snap(self, *args, **kwargs):
        return GetPriceMonitorSnapUseCase(
            price_monitor_snap_id=self.kwargs.get('price_monitor_snap_id')
        ).execute()

