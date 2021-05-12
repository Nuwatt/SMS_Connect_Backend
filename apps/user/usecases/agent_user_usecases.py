from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError

from apps.core import usecases
from apps.core.utils import update
from apps.user.exceptions import AgentUserNotFound
from apps.user.models import AgentUser
from apps.user.usecases.base_usecases import UserLoginUseCase

User = get_user_model()


class GetAgentUserUseCase(usecases.BaseUseCase):
    def __init__(self, agent_user_id: str):
        self._agent_user_id = agent_user_id

    def execute(self):
        self._factory()
        return self._agent_user

    def _factory(self):
        try:
            self._agent_user = AgentUser.objects.get(pk=self._agent_user_id)
        except AgentUser.DoesNotExist:
            raise AgentUserNotFound


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
            **self._data
        )

        # 3. create agent user
        agent_user, _created = AgentUser.objects.get_or_create(
            user=self._user
        )

        agent_user.operation_city.set(agent_data.get('operation_city'))
        agent_user.operation_country.set(agent_data.get('operation_country'))

    def is_valid(self):
        countries = self._data.get('operation_country', None)

        if countries and 'operation_city' in self._data:
            for city in self._data.get('operation_city'):
                if city.country not in countries:
                    raise ValidationError({
                        'operation_city': _('City:{} not belongs to submitted country.'.format(
                            city
                        ))
                    })


class UpdateAgentUserProfile(usecases.UpdateUseCase):
    def __init__(self, user: User, serializer):
        super().__init__(serializer, user)


class UpdateAgentUserUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, agent_user: AgentUser):
        super().__init__(serializer, agent_user)

    def _factory(self):
        # 1. pop portal user data

        if 'operation_city' in self._data:
            self._instance.operation_city.set(self._data.pop('operation_city'))

        if 'operation_country' in self._data:
            self._instance.operation_country.set(self._data.pop('operation_country'))

        # 2. update user
        update(instance=self._instance.user, data=self._data)

    def is_valid(self):
        countries = self._data.get('operation_country', self._instance.operation_country.all())

        if countries and 'operation_city' in self._data:
            for city in self._data.get('operation_city'):
                if city.country not in countries:
                    raise ValidationError({
                        'operation_city': _('City:{} not belongs to submitted country.'.format(
                            city
                        ))
                    })


class DeleteAgentUserUseCase(usecases.DeleteUseCase):
    def __init__(self, agent_user: AgentUser):
        super().__init__(agent_user)


class AgentUserLoginUseCase(UserLoginUseCase):
    pass
