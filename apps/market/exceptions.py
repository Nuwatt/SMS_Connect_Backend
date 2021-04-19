from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import NotFound


class RetailerNotFound(NotFound):
    default_detail = _('Retailer not found.')


class StoreNotFound(NotFound):
    default_detail = _('Store not found.')


class ChannelNotFound(NotFound):
    default_detail = _('Channel not found.')
