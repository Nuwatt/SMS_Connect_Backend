from django.contrib.auth import get_user_model

from apps.core import usecases
from apps.user.models import AgentUser

User = get_user_model()


class ListAgentUserUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._agent_users

    def _factory(self):
        self._agent_users = AgentUser.objects.unarchived()


class RegisterAgentUserUseCase(usecases.CreateUseCase):
    def _factory(self):
        self._user = User.objects.create_user(
            is_agent_user=True,
            ** self._data
        )
