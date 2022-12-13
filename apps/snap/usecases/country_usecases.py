from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.snap.exceptions import SnapCountryNotFound
from apps.snap.models import SnapCountry


class GetSnapCountryUseCase(usecases.BaseUseCase):
    def __init__(self, snap_country_id: str):
        self._snap_country_id = snap_country_id

    def _factory(self):
        try:
            return SnapCountry.objects.get(pk=self._snap_country_id)
        except SnapCountry.DoesNotExist:
            raise SnapCountryNotFound


class AddCountryUseCase(usecases.CreateUseCase):
    def _factory(self):
        country = SnapCountry(**self._data)
        try:
            country.full_clean()
            country.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


class UpdateCountryUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, country: SnapCountry):
        super().__init__(serializer, country)


class DeleteCountryUseCase(usecases.DeleteUseCase):
    def __init__(self, country: SnapCountry):
        super().__init__(country)


class ListCountryUseCase(usecases.BaseUseCase):
    def _factory(self):
        return SnapCountry.objects.unarchived()
