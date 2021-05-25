import csv
from io import StringIO

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import raise_errors_on_nested_writes

from apps.core.utils import update

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
        self.is_valid()
        self._factory()
        return self._instance

    def _factory(self):
        raise_errors_on_nested_writes('update', self._serializer, self._data)
        update(instance=self._instance, data=self._data)


class DeleteUseCase(BaseUseCase):

    def __init__(self, instance):
        self._instance = instance

    def execute(self):
        self.is_valid()
        self._factory()
        return self._instance

    def _factory(self):
        self._instance.archive()


class ImportCSVUseCase(CreateUseCase):
    def __init__(self, serializer):
        super().__init__(serializer)
        self._item_list = None
        self._file = StringIO(self._data.get('file').read().decode('utf-8'))

    valid_columns = []
    null_columns = []

    def execute(self):
        self.is_valid()
        self._factory()

    def is_valid(self):
        # 1. check csv has valid columns
        csv_reader = csv.DictReader(self._file)
        self._item_list = list(csv_reader)

        dict_from_csv = dict(self._item_list[0])

        # making a list from the keys of the dict
        list_of_column_names = list(dict_from_csv.keys())
        if list_of_column_names != self.valid_columns:
            columns_string = ','.join(self.valid_columns)
            raise ValidationError({
                'non_field_errors': _('CSV doesn\'t have columns in order: [{}]'.format(columns_string))
            })

        check_null_columns = self.valid_columns

        for item in sorted(self.null_columns, reverse=True):
            del check_null_columns[item]

        for item in self._item_list:
            for key in check_null_columns:
                if not item[key]:
                    raise ValidationError({
                        'non_field_errors': _('{} - has null value'.format(key))
                    })
