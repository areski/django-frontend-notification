from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _


@register.filter(name='notification_style')
def notification_style(val):
    """
    >>> notification_style(1)
    'label-inverse'

    >>> notification_style('')
    'label-success'
    """
    if val:
        return 'label-inverse'
    else:
        return 'label-success'


@register.filter(name='notification_status')
def notification_status(val):
    if val:
        return _('new').title()
    else:
        return _('read').title()
