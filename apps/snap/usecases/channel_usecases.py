from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.market.exceptions import ChannelNotFound
from apps.snap.models import SnapChannel


class GetSnapChannelUseCase(usecases.BaseUseCase):
    def __init__(self, snap_channel_id: str):
        self._channel_id = snap_channel_id

    def execute(self):
        self._factory()
        return self._channel

    def _factory(self):
        try:
            self._channel = SnapChannel.objects.get(pk=self._channel_id)
        except SnapChannel.DoesNotExist:
            raise ChannelNotFound


class AddSnapChannelUseCase(usecases.CreateUseCase):
    def _factory(self):
        channel = SnapChannel(**self._data)
        try:
            channel.full_clean()
            channel.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


class UpdateSnapChannelUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_channel: SnapChannel):
        super().__init__(serializer, snap_channel)


class DeleteSnapChannelUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_channel: SnapChannel):
        super().__init__(snap_channel)

    def _factory(self):
        self._instance.delete()


class ListSnapChannelUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._channels

    def _factory(self):
        self._channels = SnapChannel.objects.unarchived().order_by('-created')
