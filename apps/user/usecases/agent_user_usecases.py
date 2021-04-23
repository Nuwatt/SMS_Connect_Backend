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
        # 1. pop agent data
        agent_data = {
            'operation_city': self._data.pop('operation_city'),
            'operation_country': self._data.pop('operation_country')
        }

        # 2. create user
        self._user = User.objects.create_user(
            is_agent_user=True,
            ** self._data
        )

        # 3. create agent user
        agent_user, _created = AgentUser.objects.get_or_create(
            user=self._user
        )

        agent_user.operation_city.set(agent_data.get('operation_city'))
        agent_user.operation_country.set(agent_data.get('operation_country'))
