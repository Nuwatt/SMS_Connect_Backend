from apps.core import usecases
from apps.localize.exceptions import CityNotFound
from apps.localize.models import City


class GetCityUseCase(usecases.BaseUseCase):
    def __init__(self, city_id: str):
        self._city_id = city_id

    def execute(self):
        self._factory()
        return self._city

    def _factory(self):
        try:
            self._city = City.objects.get(pk=self._city_id)
        except City.DoesNotExist:
            raise CityNotFound


class AddCityUseCase(usecases.CreateUseCase):
    def _factory(self):
        City.objects.create(**self._data)


class UpdateCityUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, city: City):
        super().__init__(serializer, city)


class DeleteCityUseCase(usecases.DeleteUseCase):
    def __init__(self, city: City):
        super().__init__(city)


class ListCityUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._cities

    def _factory(self):
        self._cities = City.objects.unarchived()

