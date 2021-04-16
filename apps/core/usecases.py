from django.contrib.auth import get_user_model
from django.db.models import ProtectedError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

User = get_user_model()


class BaseUseCase:
    """
    Base Use Case
    """

    def execute(self):
        raise NotImplementedError("Subclasses should implement this!")

    def _factory(self):
        raise NotImplementedError("Subclasses should implement this!")

    def is_valid(self):
        return True


class CreateUseCase(BaseUseCase):
    def __init__(self, serializer):
        self._serializer = serializer
        self._data = self._serializer.validated_data

    def execute(self):
        self.is_valid()
        self._factory()


class UpdateUseCase(BaseUseCase):
    def __init__(self, serializer, instance):
        self._serializer = serializer
        self._data = serializer.validated_data
        self._instance = instance

    def execute(self):
        self._factory()
        return self._instance

    def _factory(self):
        raise_errors_on_nested_writes('update', self._serializer, self._data)
        info = model_meta.get_field_info(self._instance)

        for attr, value in self._data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(self._instance, attr)
                field.set(value)
            else:
                setattr(self._instance, attr, value)
        self._instance.updated_at = timezone.now()
        self._instance.save()


class DeleteUseCase(BaseUseCase):

    def __init__(self, instance):
        self._instance = instance

    def execute(self):
        self.is_valid()
        self._factory()
        return self._instance

    def _factory(self):
        try:
            self._instance.delete()
        except ProtectedError:
            raise ValidationError({'non_field_errors': _('This Item is protected cannot delete.')})
