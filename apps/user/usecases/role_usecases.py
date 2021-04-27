from django.contrib.auth import get_user_model

from apps.core import usecases
from apps.user.models import Role

User = get_user_model()


class ListRoleUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._roles

    def _factory(self):
        self._roles = Role.objects.unarchived()


class AddRoleUseCase(usecases.CreateUseCase):
    def _factory(self):
        self._role = Role.objects.create(
            **self._data
        )
