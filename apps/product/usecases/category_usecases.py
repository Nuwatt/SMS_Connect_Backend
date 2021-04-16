from apps.product.exceptions import CategoryNotFound
from apps.product.models import Category
from apps.core import usecases


class GetCategoryUseCase(usecases.BaseUseCase):
    def __init__(self, category_id: str):
        self._country_id = category_id

    def execute(self):
        self._factory()
        return self._category

    def _factory(self):
        try:
            self._category = Category.objects.get(pk=self._country_id)
        except Category.DoesNotExist:
            raise CategoryNotFound


class AddCategoryUseCase(usecases.CreateUseCase):
    def _factory(self):
        Category.objects.create(**self._data)


class UpdateCategoryUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, category: Category):
        super().__init__(serializer, category)


class DeleteCategoryUseCase(usecases.DeleteUseCase):
    def __init__(self, category: Category):
        super().__init__(category)


class ListCategoryUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._Categories

    def _factory(self):
        self._Categories = Category.objects.all()

