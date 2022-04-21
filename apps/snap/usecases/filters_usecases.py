from apps.core import usecases
from apps.snap.models import SnapPriceMonitor


class ListSKUFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'sku_id',
            'sku_name'
        ).distinct()


class ListBrandFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'brand_id',
            'brand_name'
        ).distinct()


class ListCityFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'city_id',
            'city_name'
        ).distinct()


class ListCountryFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'country_id',
            'country_name'
        ).distinct()


class ListRetailerFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'retailer_id',
            'retailer_name'
        ).distinct()


class ListStoreFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'store_id',
            'store_name'
        ).distinct()


class ListCategoryFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'category_id',
            'category_name'
        ).distinct()


class ListChannelFiltersUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapPriceMonitor.objects.values(
            'channel_id',
            'channel_name'
        ).distinct()
