from apps.core.generics import ListAPIView
from apps.user.serializers import portal_user_serializers
from apps.user.usecases import portal_user_usecases


class ListPortalUserView(ListAPIView):
    """
    Use this end-point to list all portal user
    """
    serializer_class = portal_user_serializers.ListPortalUserSerializer

    def get_queryset(self):
        return portal_user_usecases.ListPortalUserUseCase().execute()
