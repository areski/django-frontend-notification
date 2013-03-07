from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
from frontend_notification.views import notice_count


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


@register.assignment_tag(name='get_notice_count')
def get_notice_count(user):
    """tag to display notice count"""
    return notice_count(user)
