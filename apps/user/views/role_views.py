from apps.core import generics
from apps.user.serializers import role_serializers
from apps.user.usecases import role_usecases


class ListRoleView(generics.ListAPIView):
    """
    Use this end-point to list all role
    """
    serializer_class = role_serializers.ListRoleSerializer

    def get_queryset(self):
        return role_usecases.ListRoleUseCase().execute()


class AddRoleView(generics.CreateAPIView):
    """
    Use this end-point to register a new role
    """
    serializer_class = role_serializers.AddRoleSerializer

    def perform_create(self, serializer):
        return role_usecases.AddRoleUseCase(
            serializer=serializer
        ).execute()
