from apps.core import usecases
from apps.localize.exceptions import RegionNotFound
from apps.localize.models import Region


class GetRegionUseCase(usecases.BaseUseCase):
    def __init__(self, region_id: str):
        self._region_id = region_id

    def execute(self):
        self._factory()
        return self._region

    def _factory(self):
        try:
            self._region = Region.objects.get(pk=self._region_id)
        except Region.DoesNotExist:
            raise RegionNotFound


class AddRegionUseCase(usecases.CreateUseCase):
    def _factory(self):
        Region.objects.create(**self._data)


class UpdateRegionUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, region: Region):
        super().__init__(serializer, region)


class DeleteRegionUseCase(usecases.DeleteUseCase):
    def __init__(self, region: Region):
        super().__init__(region)


class ListRegionUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._countries

    def _factory(self):
        self._countries = Region.objects.unarchived()