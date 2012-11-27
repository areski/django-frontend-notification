from django.utils.translation import ugettext_lazy as _
from common.utils import Choice


class NOTICE_COLUMN_NAME(Choice):
    message = _('Message')
    notice_type = _('Notice type')
    sender = _('Sender')
    date_field = _('Date')
