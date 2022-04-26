from django.db.models import Max, Count, Min, Avg
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.snap.models import SnapPriceMonitor, SnapSKU


class PriceMonitorSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, sku_provided):
        self._sku_provided = sku_provided

    def _final_data(self, query):
        if not self._sku_provided:
            snap_skus = SnapSKU.objects.filter(is_archived=False).values('id')[:10]
            snap_ids = [item.get('id') for item in snap_skus]
            return query.filter(sku_id__in=snap_ids)
        return query


# city
class CityMaxPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
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
            'city_name'
        ).unarchived()

        return self._final_data(query)


class CityMinPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Min('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'city_name'
        ).unarchived()

        return self._final_data(query)


class CityMeanPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Avg('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'city_name'
        ).unarchived()

        return self._final_data(query)


# channel
class ChannelMaxPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
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
            'channel_name'
        ).unarchived()

        return self._final_data(query)


class ChannelMinPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Min('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'channel_name'
        ).unarchived()

        return self._final_data(query)


class ChannelMeanPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Avg('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'channel_name'
        ).unarchived()

        return self._final_data(query)


# brand
class BrandMaxPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
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
            'brand_name'
        ).unarchived()

        return self._final_data(query)


class BrandMinPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Min('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'brand_name'
        ).unarchived()

        return self._final_data(query)


class BrandMeanPriceMonitorSnapReportUseCase(PriceMonitorSnapReportUseCase):
    def _factory(self):
        query = SnapPriceMonitor.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            value=Avg('max'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'value',
            'brand_name'
        ).unarchived()

        return self._final_data(query)
