from apps.core import usecases
from apps.localize.exceptions import NationalityNotFound
from apps.localize.models import Nationality


class GetCountryUseCase(usecases.BaseUseCase):
    def __init__(self, nationality_id: str):
        self._nationality_id = nationality_id

    def execute(self):
        self._factory()
        return self._nationality

    def _factory(self):
        try:
            self._nationality = Nationality.objects.get(pk=self._nationality_id)
        except Nationality.DoesNotExist:
            raise NationalityNotFound


class AddNationalityUseCase(usecases.CreateUseCase):
    def _factory(self):
        Nationality.objects.create(**self._data)


class UpdateNationalityUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, nationality: Nationality):
        super().__init__(serializer, nationality)


class DeleteNationalityUseCase(usecases.DeleteUseCase):
    def __init__(self, nationality: Nationality):
        super().__init__(nationality)


class ListCountryUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._countries

    def _factory(self):
        self._countries = Nationality.objects.unarchived()

