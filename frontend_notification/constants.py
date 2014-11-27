from django.utils.translation import ugettext_lazy as _
from django_lets_go.utils import Choice


class NOTICE_TYPE(Choice):
    READ = 0, _('Read')
    NEW = 1, _('New')
    ALL = 2, _('All')
