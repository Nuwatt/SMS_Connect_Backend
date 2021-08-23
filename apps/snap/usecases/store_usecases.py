from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.market.exceptions import ChannelNotFound
from apps.snap.models import SnapStore


class GetSnapStoreUseCase(usecases.BaseUseCase):
    def __init__(self, snap_store_id: str):
        self._store_id = snap_store_id

    def execute(self):
        self._factory()
        return self._store

    def _factory(self):
        try:
            self._store = SnapStore.objects.get(pk=self._store_id)
        except SnapStore.DoesNotExist:
            raise ChannelNotFound


class AddSnapStoreUseCase(usecases.CreateUseCase):
    def _factory(self):
        store_names = self._data.get('name')
        stores = []
        for name in store_names:
            store = SnapStore(
                retailer=self._data.get('retailer'),
                city=self._data.get('city'),
                channel=self._data.get('channel'),
                name=name
            )
            try:
                store.full_clean()
                stores.append(store)
            except DjangoValidationError as e:
                raise ValidationError(e.message_dict)
        SnapStore.objects.bulk_create(stores)


class UpdateSnapStoreUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_store: SnapStore):
        super().__init__(serializer, snap_store)


class DeleteSnapStoreUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_store: SnapStore):
        super().__init__(snap_store)

    def _factory(self):
        self._instance.delete()


class ListSnapStoreUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._stores

    def _factory(self):
        self._stores = SnapStore.objects.unarchived().select_related(
            'retailer',
            'city',
            'city__country'
        ).order_by('-created')

