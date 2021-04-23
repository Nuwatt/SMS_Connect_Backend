from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.terms_and_conditions.exceptions import TermsAndConditionsNotFound
from apps.terms_and_conditions.models import TermsAndConditions


class GetTermsAndConditionsUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._terms_and_conditions

    def _factory(self):
        self._terms_and_conditions = TermsAndConditions.objects.first()
        if not self._terms_and_conditions:
            raise TermsAndConditionsNotFound


class AddTermsAndConditionsUseCase(usecases.CreateUseCase):
    def _factory(self):
        terms_and_conditions = TermsAndConditions(**self._data)
        try:
            terms_and_conditions.full_clean()
            terms_and_conditions.save()
        except DjangoValidationError as e:
            raise ValidationError(e.message_dict)


class UpdateTermsAndConditionsUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, terms_and_conditions: TermsAndConditions):
        super().__init__(serializer, terms_and_conditions)


class DeleteTermsAndConditionsUseCase(usecases.DeleteUseCase):
    def __init__(self, terms_and_conditions: TermsAndConditions):
        super().__init__(terms_and_conditions)


class TermsAndConditionsDetailUseCase(usecases.BaseUseCase):
    def __init__(self, terms_and_conditions: TermsAndConditions):
        self._terms_and_conditions = terms_and_conditions

    def execute(self):
        self._factory()
        return self._terms_and_conditions

    def _factory(self):
        if self._terms_and_conditions.is_archived:
            raise TermsAndConditionsNotFound

