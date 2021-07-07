from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.market.exceptions import ChannelNotFound
from apps.market.models import Channel, Store
from apps.market.models import Retailer


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
        store_names = self._data.get('name')
        stores = []
        for name in store_names:
            store = Store(
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
        Store.objects.bulk_create(stores)


class AddStoreRetailerUseCase(usecases.CreateUseCase):
    def _factory(self):
        retailer, created = Retailer.objects.get_or_create(
            name=self._data.get('retailer'),
            is_archived=False
        )
        store = Store(
            retailer=retailer,
            channel=self._data.get('channel'),
            city=self._data.get('city'),
            name=self._data.get('name')
        )
        try:
            store.full_clean()
            store.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


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
        self._stores = Store.objects.unarchived().select_related(
            'retailer',
            'city',
            'city__country'
        ).order_by('-created')


class ListStoreForAgentUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._stores

    def _factory(self):
        self._stores = Store.objects.unarchived().select_related(
            'retailer'
        )

