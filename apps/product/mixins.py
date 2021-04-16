from apps.product.usecases.brand_usecases import GetBrandUseCase
from apps.product.usecases.category_usecases import GetCategoryUseCase
from apps.product.usecases.sku_usecases import GetSKUUseCase
from apps.localize.usecases.area_usecases import GetAreaUseCase
from apps.localize.usecases.city_usecases import GetCityUseCase
from apps.localize.usecases.country_usecases import GetCountryUseCase


class BrandMixin:
    def get_brand(self, *args, **kwargs):
        return GetBrandUseCase(
            brand_id=self.kwargs.get('brand_id')
        ).execute()


class SKUMixin:
    def get_sku(self, *args, **kwargs):
        return GetSKUUseCase(
            sku_id=self.kwargs.get('sku_id')
        ).execute()


class CategoryMixin:
    def get_category(self, *args, **kwargs):
        return GetCategoryUseCase(
            category_id=self.kwargs.get('category_id')
        ).execute()
