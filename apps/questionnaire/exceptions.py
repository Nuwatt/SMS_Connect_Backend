from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class QuestionnaireNotFound(NotFound):
    default_detail = _('Questionnaire not found.')


class QuestionnaireTypeNotFound(NotFound):
    default_detail = _('Questionnaire Type not found.')
