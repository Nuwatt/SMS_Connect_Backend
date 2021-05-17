from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class ResponseNotFound(NotFound):
    default_detail = _('Response not found.')

