from django.contrib.auth import get_user_model

from apps.core import usecases
from apps.core.utils import update
from apps.user.exceptions import PortalUserNotFound, LoginFailed
from apps.user.models import PortalUser
from apps.user.usecases.base_usecases import UserLoginUseCase

User = get_user_model()


class GetPortalUserUseCase(usecases.BaseUseCase):
    def __init__(self, portal_user_id: str):
        self._portal_user_id = portal_user_id

    def execute(self):
        self._factory()
        return self._portal_user

    def _factory(self):
        try:
            self._portal_user = PortalUser.objects.get(pk=self._portal_user_id)
        except PortalUser.DoesNotExist:
            raise PortalUserNotFound


class ListPortalUserUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._portal_users

    def _factory(self):
        self._portal_users = PortalUser.objects.unarchived().order_by('-created')


class RegisterPortalUserUseCase(usecases.CreateUseCase):
    def _factory(self):
        # 1. pop portal user data
        portal_user_data = {
            'role': self._data.pop('role'),
            'position': self._data.pop('position'),
        }

        # 2. create user
        self._user = User.objects.create_user(
            is_portal_user=True,
            **self._data
        )

        # 3. create portal user
        portal_user, _created = PortalUser.objects.update_or_create(
            user=self._user,
            defaults=portal_user_data
        )


class UpdatePortalUserUseCase(usecases.UpdateUseCase):
    def __init__(self, serializer, portal_user: PortalUser):
        super().__init__(serializer, portal_user)

    def _factory(self):
        # 1. pop portal user data
        portal_user_data = {}

        if 'role' in self._data:
            portal_user_data['role'] = self._data.pop('role')

        if 'position' in self._data:
            portal_user_data['position'] = self._data.pop('position')

        # 2. update user
        update(instance=self._instance.user, data=self._data)

        # 3. update portal user
        if portal_user_data:
            update(instance=self._instance, data=portal_user_data)


class DeletePortalUserUseCase(usecases.DeleteUseCase):
    def __init__(self, portal_user: PortalUser):
        super().__init__(portal_user)


class PortalUserLoginUseCase(UserLoginUseCase):
    def _validate(self, user):
        if not user.is_portal_user:
            raise LoginFailed
        super(PortalUserLoginUseCase, self)._validate(user)


class UploadPortalUserAvatarUseCase(usecases.CreateUseCase):
    def __init__(self, portal_user: PortalUser, serializer):
        super().__init__(serializer)
        self._portal_user = portal_user

    def _factory(self):
        user = self._portal_user.user
        user.avatar = self._data.get('avatar')
        user.save()

    def execute(self):
        super(UploadPortalUserAvatarUseCase, self).execute()
        return self._portal_user
