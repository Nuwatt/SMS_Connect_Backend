from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class QuestionNotFound(NotFound):
    default_detail = _('Question not found.')
