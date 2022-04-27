from apps.core import usecases


class ListSKUFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'sku_id',
            'sku_name'
        ).distinct()


class ListBrandFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'brand_id',
            'brand_name'
        ).distinct()


class ListCityFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'city_id',
            'city_name'
        ).distinct()


class ListCountryFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'country_id',
            'country_name'
        ).distinct()


class ListRetailerFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'retailer_id',
            'retailer_name'
        ).distinct()


class ListStoreFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'store_id',
            'store_name'
        ).distinct()


class ListCategoryFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'category_id',
            'category_name'
        ).distinct()


class ListChannelFiltersUseCase(usecases.BaseUseCase):
    def __init__(self, snap_model):
        self._snap_model = snap_model

    def _factory(self):
        return self._snap_model.objects.values(
            'channel_id',
            'channel_name'
        ).distinct()
