from django.db.models import Max, Count
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.snap.models import SnapPriceMonitor, SnapSKU


class CityMaxPriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, sku_provided):
        self._sku_provided = sku_provided

    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Max('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'city_name',
        ).unarchived()

        if not self._sku_provided:
            snap_skus = SnapSKU.objects.filter(is_archived=False).values('id')[:10]
            snap_ids = [item.get('id') for item in snap_skus]
            return query.filter(sku_id__in=snap_ids)
        return query
