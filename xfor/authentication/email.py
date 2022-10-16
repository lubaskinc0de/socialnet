from templated_mail.mail import BaseEmailMessage
from .tokens import authentication_token
from djoser.utils import encode_uid
from django.conf import settings
from django.contrib.auth.models import User

class ActivationEmail(BaseEmailMessage):
    template_name = "authentication/activation.html"

    def get_context_data(self):
        context = super().get_context_data()

        user: User = context.get('user')
        uid = encode_uid(user.id)
        token = authentication_token.make_token(user)

        url: str = settings.USER_ACTIVATION_URL.format(uid, token)

        context['url'] = url
        context['sitename'] = settings.AUTHENTICATION_SITENAME
        return context