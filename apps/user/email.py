from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage

from apps.user import utils


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/reset_password.html"

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get("user")
        context["uid"] = utils.encode_uid(user.pk)
        context["token"] = default_token_generator.make_token(user)
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(
            context.get('uid'),
            context.get('token')
        )
        return context


class PasswordResetConfirmationEmail(BaseEmailMessage):
    template_name = "email/reset_password_confirmation.html"


class PasswordChangeConfirmationEmail(BaseEmailMessage):
    template_name = "email/change_password_confirmation.html"


class SupportEmail(BaseEmailMessage):
    template_name = "email/support.html"
