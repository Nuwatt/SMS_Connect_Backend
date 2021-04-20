from apps.core.generics import ListAPIView, CreateAPIView
from apps.user.serializers import agent_user_serializers
from apps.user.usecases import agent_user_usecases


class ListAgentUserView(ListAPIView):
    """
    Use this end-point to list all agent user
    """
    serializer_class = agent_user_serializers.ListAgentUserSerializer

    def get_queryset(self):
        return agent_user_usecases.ListAgentUserUseCase().execute()


class RegisterAgentUserView(CreateAPIView):
    """
    Use this end-point to register a new agent
    """
    serializer_class = agent_user_serializers.RegisterAgentUserSerializer

    def perform_create(self, serializer):
        return agent_user_usecases.RegisterAgentUserUseCase(
            serializer=serializer
        ).execute()
