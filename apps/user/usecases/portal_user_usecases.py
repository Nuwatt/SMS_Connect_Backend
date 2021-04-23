from django.contrib.auth import get_user_model

from apps.core import usecases
from apps.user.models import PortalUser

User = get_user_model()


class ListPortalUserUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._portal_users

    def _factory(self):
        self._portal_users = PortalUser.objects.unarchived()


class RegisterPortalUserUseCase(usecases.CreateUseCase):
    def _factory(self):
        # 1. pop portal user data
        portal_user_data = {
            'role': self._data.pop('role')
        }

        # 2. create user
        self._user = User.objects.create_user(
            is_portal_user=True,
            **self._data
        )

        # 3. create portal user
        portal_user, _created = PortalUser.objects.update_or_create(
            user=self._user,
            defaults=portal_user_data
        )
