from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.product.exceptions import BrandNotFound
from apps.snap.models import SnapBrand


class GetSnapBrandUseCase(usecases.BaseUseCase):
    def __init__(self, snap_brand_id: str):
        self._snap_brand_id = snap_brand_id

    def execute(self):
        self._factory()
        return self._snap_brand

    def _factory(self):
        try:
            self._snap_brand = SnapBrand.objects.get(pk=self._snap_brand_id)
        except SnapBrand.DoesNotExist:
            raise BrandNotFound


class AddSnapBrandUseCase(usecases.CreateUseCase):
    def _factory(self):
        brand = SnapBrand(
            **self._data
        )
        try:
            brand.full_clean()
            brand.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


class UpdateSnapBrandUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_brand: SnapBrand):
        super().__init__(serializer, snap_brand)


class DeleterSnapBrandUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_brand: SnapBrand):
        super().__init__(snap_brand)

    def _factory(self):
        self._instance.delete()


class ListSnapBrandUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._brands

    def _factory(self):
        self._brands = SnapBrand.objects.unarchived().order_by('-created')

