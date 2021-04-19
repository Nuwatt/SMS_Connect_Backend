from apps.core import usecases
from apps.market.exceptions import ChannelNotFound
from apps.market.models import Store


class GetStoreUseCase(usecases.BaseUseCase):
    def __init__(self, store_id: str):
        self._store_id = store_id

    def execute(self):
        self._factory()
        return self._store

    def _factory(self):
        try:
            self._store = Store.objects.get(pk=self._store_id)
        except Store.DoesNotExist:
            raise ChannelNotFound


class AddStoreUseCase(usecases.CreateUseCase):
    def _factory(self):
        Store.objects.create(**self._data)


class UpdateStoreUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, store: Store):
        super().__init__(serializer, store)


class DeleteStoreUseCase(usecases.DeleteUseCase):
    def __init__(self, store: Store):
        super().__init__(store)


class ListStoreUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._stores

    def _factory(self):
        self._stores = Store.objects.unarchived()

