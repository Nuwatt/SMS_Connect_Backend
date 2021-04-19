from apps.market.exceptions import RetailerNotFound
from apps.market.models import Retailer
from apps.core import usecases


class GetRetailerUseCase(usecases.BaseUseCase):
    def __init__(self, retailer_id: str):
        self._retailer_id = retailer_id

    def execute(self):
        self._factory()
        return self._retailer

    def _factory(self):
        try:
            self._retailer = Retailer.objects.get(pk=self._retailer_id)
        except Retailer.DoesNotExist:
            raise RetailerNotFound


class AddRetailerUseCase(usecases.CreateUseCase):
    def _factory(self):
        Retailer.objects.create(**self._data)


class UpdateRetailerUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, retailer: Retailer):
        super().__init__(serializer, retailer)


class DeleteRetailerUseCase(usecases.DeleteUseCase):
    def __init__(self, retailer: Retailer):
        super().__init__(retailer)


class ListRetailerUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._retailers

    def _factory(self):
        self._retailers = Retailer.objects.unarchived()
