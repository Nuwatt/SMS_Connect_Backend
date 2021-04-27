from apps.localize.usecases.area_usecases import GetAreaUseCase
from apps.localize.usecases.city_usecases import GetCityUseCase
from apps.localize.usecases.country_usecases import GetCountryUseCase
from apps.localize.usecases.region_usecases import GetRegionUseCase


class CountryMixin:
    def get_country(self, *args, **kwargs):
        return GetCountryUseCase(
            country_id=self.kwargs.get('country_id')
        ).execute()


class CityMixin:
    def get_city(self, *args, **kwargs):
        return GetCityUseCase(
            city_id=self.kwargs.get('city_id')
        ).execute()


class AreaMixin:
    def get_area(self, *args, **kwargs):
        return GetAreaUseCase(
            area_id=self.kwargs.get('area_id')
        ).execute()


class RegionMixin:
    def get_region(self, *args, **kwargs):
        return GetRegionUseCase(
            area_id=self.kwargs.get('region_id')
        ).execute()
