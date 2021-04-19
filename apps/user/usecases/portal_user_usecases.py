from apps.core import usecases
from apps.user.models import PortalUser


class ListPortalUserUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._portal_users

    def _factory(self):
        self._portal_users = PortalUser.objects.unarchived()

