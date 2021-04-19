from apps.core import usecases
from apps.market.exceptions import ChannelNotFound
from apps.market.models import Store, Channel


class GetChannelUseCase(usecases.BaseUseCase):
    def __init__(self, channel_id: str):
        self._channel_id = channel_id

    def execute(self):
        self._factory()
        return self._store

    def _factory(self):
        try:
            self._store = Channel.objects.get(pk=self._channel_id)
        except Channel.DoesNotExist:
            raise ChannelNotFound


class AddChannelUseCase(usecases.CreateUseCase):
    def _factory(self):
        Channel.objects.create(**self._data)


class UpdateChannelUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, store: Store):
        super().__init__(serializer, store)


class DeleteChannelUseCase(usecases.DeleteUseCase):
    def __init__(self, store: Store):
        super().__init__(store)


class ListChannelUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._channels

    def _factory(self):
        self._channels = Channel.objects.all()

