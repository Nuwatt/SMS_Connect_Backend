from django.core.validators import _lazy_re_compile
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

from apps.core.validators import WordValidator


@deconstructible
class QuestionTypeValidator(WordValidator):
    message = _('Enter a valid question type.')
    regex_message = _('Accepted words with letters digits and &.')
    regex = _lazy_re_compile(
        r'^[aA-zZ0-9\s\&]+$'
    )


@deconstructible
class QuestionStatementValidator(WordValidator):
    message = _('Enter a valid question statement.')
    regex_message = _('Accepted words with letters, digits and ?,.@()')
    regex = _lazy_re_compile(
        r'^[aA-zZ0-9\s\?\,\.\@\(\)]+$'
    )


@deconstructible
class QuestionOptionValidator(WordValidator):
    message = _('Enter a valid question option.')
    regex_message = _('Accepted words with letters, digits')
    regex = _lazy_re_compile(
        r'^[aA-zZ0-9]+$'
    )


validate_question_type = QuestionTypeValidator()
validate_question_statement = QuestionStatementValidator()
validate_question_option = QuestionOptionValidator()
