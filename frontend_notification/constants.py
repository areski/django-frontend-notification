from django.utils.translation import ugettext_lazy as _
from common.utils import Choice


class NOTICE_COLUMN_NAME(Choice):
    message = _('message')
    notice_type = _('notice type')
    sender = _('sender')
    date_field = _('date')


class NOTICE_TYPE(Choice):
    READ = 0, _('read').title()
    NEW = 1, _('new').title()
    ALL = 2, _('all').title()
