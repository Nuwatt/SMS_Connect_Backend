from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country
from apps.product.exceptions import SKUNotFound
from apps.product.models import SKU, Category, Brand
from apps.snap.models import SnapSKU


class GetSnapSKUUseCase(usecases.BaseUseCase):
    def __init__(self, snap_sku_id: str):
        self._snap_sku_id = snap_sku_id

    def execute(self):
        self._factory()
        return self._sku

    def _factory(self):
        try:
            self._sku = SnapSKU.objects.get(pk=self._snap_sku_id)
        except SnapSKU.DoesNotExist:
            raise SKUNotFound


class AddSnapSKUUseCase(usecases.CreateUseCase):
    def _factory(self):
        sku_names = self._data.get('name')
        for name in sku_names:
            sku = SKU(
                brand=self._data.get('brand'),
                category=self._data.get('category'),
                name=name
            )
            try:
                sku.clean()
            except DjangoValidationError as e:
                raise ValidationError(e.message_dict)
            sku.save()

            # save country
            sku.country.set(self._data.get('country'))


class UpdateSnapSKUUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_sku: SnapSKU):
        super().__init__(serializer, snap_sku)


class DeleteSnapSKUUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_sku: SnapSKU):
        super().__init__(snap_sku)

    def _factory(self):
        self._instance.delete()


class ListSnapSKUUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._sku_list

    def _factory(self):
        self._sku_list = SnapSKU.objects.unarchived().prefetch_related(
            'country'
        ).select_related(
            'brand',
            'category',
        ).order_by('-created')
