from django.db import transaction

from apps.product.exceptions import SKUNotFound
from apps.product.models import SKU, Category, Brand
from apps.core import usecases


class GetSKUUseCase(usecases.BaseUseCase):
    def __init__(self, sku_id: str):
        self._area_id = sku_id

    def execute(self):
        self._factory()
        return self._sku

    def _factory(self):
        try:
            self._sku = SKU.objects.get(pk=self._area_id)
        except SKU.DoesNotExist:
            raise SKUNotFound


class AddSKUUseCase(usecases.CreateUseCase):
    def _factory(self):
        sku_names = self._data.get('name')
        skus = []
        for name in sku_names:
            store = SKU(
                category=self._data.get('category'),
                brand=self._data.get('brand'),
                name=name
            )
            skus.append(store)
        SKU.objects.bulk_create(skus)


class UpdateSKUUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, sku: SKU):
        super().__init__(serializer, sku)


class DeleteSKUUseCase(usecases.DeleteUseCase):
    def __init__(self, sku: SKU):
        super().__init__(sku)


class ListSKUUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._sku_list

    def _factory(self):
        self._sku_list = SKU.objects.unarchived().select_related(
            'brand',
            'category'
        )


class ImportSKUUseCase(usecases.ImportCSVUseCase):
    valid_columns = ['SKU Name', 'Brand Name', 'Category Name']

    @transaction.atomic
    def _factory(self):
        for item in self._item_list:
            category, created = Category.objects.get_or_create(name=item.get('Category Name'))
            brand, created = Brand.objects.get_or_create(name=item.get('Brand Name'), category=category)
            sku, created = SKU.objects.update_or_create(
                name=item.get('SKU Name'),
                defaults={
                    'brand': brand,
                    'category': category,
                }
            )
