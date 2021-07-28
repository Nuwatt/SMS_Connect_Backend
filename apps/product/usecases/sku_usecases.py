from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.localize.models import Country
from apps.product.exceptions import SKUNotFound
from apps.product.models import SKU, Category, Brand


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
        # skus = []

        # last_id = last_id_for_bulk_create(initial='SKU', model=SKU)

        for name in sku_names:
            # next_id = last_id + 1
            sku = SKU(
                # id='SKU{0:04}'.format(next_id),
                brand=self._data.get('brand'),
                category=self._data.get('category'),
                name=name
            )
            try:
                sku.clean()
            except DjangoValidationError as e:
                raise ValidationError(e.message_dict)
            # skus.append(sku)
            # last_id = next_id
            sku.save()

            # save country
            sku.country.set(self._data.get('country'))
        # SKU.objects.bulk_create(skus)


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
        self._sku_list = SKU.objects.unarchived().prefetch_related(
            'country'
        ).select_related(
            'brand',
            'category',
        ).order_by('-created')


class ImportSKUUseCase(usecases.ImportCSVUseCase):
    valid_columns = ['SKU Name', 'Brand Name', 'Category Name', 'Country']
    null_columns = ['Country']

    @transaction.atomic
    def _factory(self):
        for item in self._item_list:
            countries_data = None
            category, created = Category.objects.get_or_create(
                name=item.get('Category Name'),
                is_archived=False
            )
            brand, created = Brand.objects.get_or_create(
                name=item.get('Brand Name'),
                is_archived=False
            )

            sku, created = SKU.objects.get_or_create(
                name=item.get('SKU Name'),
                brand=brand,
                category=category,
                is_archived=False
            )

            if item.get('Country'):
                countries_data = item.get('Country').split(',')

            if countries_data:
                countries = []
                for name in countries_data:
                    try:
                        countries.append(Country.objects.get(name=name, is_archived=False))
                    except Country.DoesNotExist:
                        raise ValidationError({
                            'country': _('Country:{} doesn\'t exists.'.format(name))
                        })
                sku.country.set(countries)

