from apps.core import usecases
from apps.localize.exceptions import AreaNotFound
from apps.localize.models import Area


class GetAreaUseCase(usecases.BaseUseCase):
    def __init__(self, area_id: str):
        self._area_id = area_id

    def execute(self):
        self._factory()
        return self._area

    def _factory(self):
        try:
            self._area = Area.objects.get(pk=self._area_id)
        except Area.DoesNotExist:
            raise AreaNotFound


class AddAreaUseCase(usecases.CreateUseCase):
    def _factory(self):
        Area.objects.create(**self._data)


class UpdateAreaUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, area: Area):
        super().__init__(serializer, area)


class DeleteAreaUseCase(usecases.DeleteUseCase):
    def __init__(self, area: Area):
        super().__init__(area)


class ListAreaUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._areas

    def _factory(self):
        self._areas = Area.objects.all()
