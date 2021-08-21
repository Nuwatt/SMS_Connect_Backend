from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.product.exceptions import CategoryNotFound
from apps.snap.models import SnapCategory


class GetSnapCategoryUseCase(usecases.BaseUseCase):
    def __init__(self, snap_category_id: str):
        self._snap_category_id = snap_category_id

    def execute(self):
        self._factory()
        return self._category

    def _factory(self):
        try:
            self._category = SnapCategory.objects.get(pk=self._snap_category_id)
        except SnapCategory.DoesNotExist:
            raise CategoryNotFound


class AddSnapCategoryUseCase(usecases.CreateUseCase):
    def _factory(self):
        category = SnapCategory(**self._data)
        try:
            category.clean()
            category.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


class UpdateSnapCategoryUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, snap_category: SnapCategory):
        super().__init__(serializer, snap_category)


class DeleteSnapCategoryUseCase(usecases.DeleteUseCase):
    def __init__(self, snap_category: SnapCategory):
        super().__init__(snap_category)

    def _factory(self):
        self._instance.delete()


class ListSnapCategoryUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._categories

    def _factory(self):
        self._categories = SnapCategory.objects.unarchived().order_by('-created')
