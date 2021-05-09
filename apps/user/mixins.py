from apps.user.usecases.agent_user_usecases import GetAgentUserUseCase
from apps.user.usecases.portal_user_usecases import GetPortalUserUseCase


class AgentUserMixin:
    def get_agent_user(self, *args, **kwargs):
        return GetAgentUserUseCase(
            agent_user_id=self.kwargs.get('agent_user_id')
        ).execute()


class PortalUserMixin:
    def get_portal_user(self, *args, **kwargs):
        return GetPortalUserUseCase(
            portal_user_id=self.kwargs.get('portal_user_id')
        ).execute()
