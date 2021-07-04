from apps.localize.usecases.city_usecases import GetCityUseCase
from apps.localize.usecases.country_usecases import GetCountryUseCase


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
