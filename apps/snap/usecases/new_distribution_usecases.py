from django.db.models import Avg
from django.db.models.functions import TruncMonth

from apps.core import usecases
from apps.snap.models import SnapSKU, SnapDistribution


class DistributionSnapReportUseCase(usecases.BaseUseCase):
    def __init__(self, sku_provided):
        self._sku_provided = sku_provided

    def _final_data(self, query):
        if not self._sku_provided:
            snap_skus = SnapSKU.objects.filter(is_archived=False).values('id')[:10]
            snap_ids = [item.get('id') for item in snap_skus]
            return query.filter(sku_id__in=snap_ids)
        return query


# city
class DistributionSnapCityReportUseCase(DistributionSnapReportUseCase):
    def _factory(self):
        query = SnapDistribution.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            total_distribution_value=Avg('total_distribution'),
            shelf_share_value=Avg('shelf_share'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'total_distribution_value',
            'shelf_share_value',
            'city_name'
        ).unarchived()

        return self._final_data(query)


# brand
class DistributionSnapBrandReportUseCase(DistributionSnapReportUseCase):
    def _factory(self):
        query = SnapDistribution.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            total_distribution_value=Avg('total_distribution'),
            shelf_share_value=Avg('shelf_share'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'total_distribution_value',
            'shelf_share_value',
            'brand_name'
        ).unarchived()

        return self._final_data(query)


# channel
class DistributionSnapChannelReportUseCase(DistributionSnapReportUseCase):
    def _factory(self):
        query = SnapDistribution.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            total_distribution_value=Avg('total_distribution'),
            shelf_share_value=Avg('shelf_share'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'total_distribution_value',
            'shelf_share_value',
            'channel_name'
        ).unarchived()

        return self._final_data(query)


# sku
class DistributionSnapSKUReportUseCase(DistributionSnapReportUseCase):
    def _factory(self):
        query = SnapDistribution.objects.annotate(
            month=TruncMonth('date')
        ).values(
            'month'
        ).annotate(
            total_distribution_value=Avg('total_distribution'),
            shelf_share_value=Avg('shelf_share'),
        ).values(
            'sku_name',
            'sku_id',
            'month',
            'total_distribution_value',
            'shelf_share_value'
        ).unarchived()

        return self._final_data(query)

