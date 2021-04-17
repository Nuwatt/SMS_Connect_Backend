from apps.core import usecases
from apps.user.models import AgentUser


class ListAgentUserUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._agent_users

    def _factory(self):
        self._agent_users = AgentUser.objects.all()

