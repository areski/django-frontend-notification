from django.utils.translation import ugettext_lazy as _
from common.utils import Choice


class NOTICE_COLUMN_NAME(Choice):
    message = _('message')
    notice_type = _('notice type')
    sender = _('sender')
    date_field = _('date')
