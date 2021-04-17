from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from apps.core import usecases
from apps.user.exceptions import UserInactive, LoginFailed

User = get_user_model()


class UserSignupUseCase(usecases.CreateUseCase):

    def _factory(self):
        self._user = User.objects.create_user(
            **self._data
        )


class UserLoginUseCase(usecases.CreateUseCase):
    def execute(self):
        super(UserLoginUseCase, self).execute()
        return self._result

    def _factory(self):
        # 1. authenticate user
        user = authenticate(
            email=self._data.get('email'),
            password=self._data.get('password')
        )

        # 1a. if not authenticated raise LoginFailed Exception
        if not user:
            raise LoginFailed

        # 1b. if user is not active raise UserInactive Exception
        if not user.is_active:
            raise UserInactive

        # 3. Get user token for user
        user_token = RefreshToken.for_user(user)
        refresh_token = str(user_token)
        access_token = str(user_token.access_token)

        self._result = {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'detail': user
        }


class ListUserUseCase(usecases.BaseUseCase):
    def execute(self):
        self._factory()
        return self._users

    def _factory(self):
        self._users = User.objects.all()

