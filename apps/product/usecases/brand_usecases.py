from apps.product.exceptions import BrandNotFound
from apps.product.models import Brand
from apps.core import usecases


class GetBrandUseCase(usecases.BaseUseCase):
    def __init__(self, brand_id: str):
        self._brand_id = brand_id

    def execute(self):
        self._factory()
        return self._city

    def _factory(self):
        try:
            self._city = Brand.objects.get(pk=self._brand_id)
        except Brand.DoesNotExist:
            raise BrandNotFound


class AddBrandUseCase(usecases.CreateUseCase):
    def _factory(self):
        Brand.objects.create(**self._data)


class UpdateBrandUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, brand: Brand):
        super().__init__(serializer, brand)


class DeleteBrandUseCase(usecases.DeleteUseCase):
    def __init__(self, brand: Brand):
        super().__init__(brand)


class ListBrandUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._brands

    def _factory(self):
        self._brands = Brand.objects.all()

