from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException, NotFound


class UserInactive(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('User is not active.')
    default_code = 'user_not_active'


class LoginFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Incorrect login credentials')
    default_code = 'login_failed'


class PortalUserNotFound(NotFound):
    default_detail = _('Portal User not found.')


class AgentUserNotFound(NotFound):
    default_detail = _('Agent User not found.')

