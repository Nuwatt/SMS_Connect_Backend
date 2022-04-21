from apps.core import usecases
from apps.snap.exceptions import SnapCityNotFound
from apps.snap.models import SnapCity


class GetSnapCityUseCase(usecases.BaseUseCase):
    def __init__(self, snap_city_id: str):
        self._snap_city_id = snap_city_id

    def execute(self):
        self._factory()
        return self._city

    def _factory(self):
        try:
            self._city = SnapCity.objects.get(pk=self._snap_city_id)
        except SnapCity.DoesNotExist:
            raise SnapCityNotFound


class AddSnapCityUseCase(usecases.CreateUseCase):
    def _factory(self):
        SnapCity.objects.create(**self._data)


class UpdateSnapCityUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_city: SnapCity):
        super().__init__(serializer, snap_city)


class DeleteSnapCityUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_city: SnapCity):
        super().__init__(snap_city)


class ListSnapCityUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapCity.objects.values(
            'id',
            'name',
            'country_id',
        ).unarchived()
