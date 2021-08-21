import csv

from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError

from apps.localize.models import Country, City
from apps.market.exceptions import RetailerNotFound
from apps.core import usecases
from apps.snap.models import SnapRetailer
from apps.user.models import AgentUser


class GetSnapRetailerUseCase(usecases.BaseUseCase):
    def __init__(self, snap_retailer_id: str):
        self._retailer_id = snap_retailer_id

    def execute(self):
        self._factory()
        return self._retailer

    def _factory(self):
        try:
            self._retailer = SnapRetailer.objects.get(pk=self._retailer_id)
        except SnapRetailer.DoesNotExist:
            raise RetailerNotFound


class AddSnapRetailerUseCase(usecases.CreateUseCase):
    def _factory(self):
        retailers = []
        for name in self._data.get('name'):
            retailer = SnapRetailer(
                name=name,
            )
            try:
                retailer.full_clean()
            except DjangoValidationError as e:
                raise ValidationError(e.message_dict)
            retailers.append(retailer)
        SnapRetailer.objects.bulk_create(retailers)


class UpdateSnapRetailerUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_retailer: SnapRetailer):
        super().__init__(serializer, snap_retailer)


class DeleteSnapRetailerUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_retailer: SnapRetailer):
        super().__init__(snap_retailer)

    def _factory(self):
        self._instance.delete()


class ListSnapRetailerUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._retailers

    def _factory(self):
        self._retailers = SnapRetailer.objects.unarchived().order_by('-created')


class BasicListSnapRetailerUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._retailers

    def _factory(self):
        self._retailers = SnapRetailer.objects.unarchived()
