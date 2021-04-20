from apps.core.generics import ListAPIView, CreateAPIView
from apps.user.serializers import portal_user_serializers
from apps.user.usecases import portal_user_usecases


class ListPortalUserView(ListAPIView):
    """
    Use this end-point to list all portal user
    """
    serializer_class = portal_user_serializers.ListPortalUserSerializer

    def get_queryset(self):
        return portal_user_usecases.ListPortalUserUseCase().execute()


class RegisterPortalUserView(CreateAPIView):
    """
    Use this end-point to register a new Portal user
    """
    serializer_class = portal_user_serializers.RegisterPortalUserSerializer

    def perform_create(self, serializer):
        return portal_user_usecases.RegisterPortalUserUseCase(
            serializer=serializer
        ).execute()
