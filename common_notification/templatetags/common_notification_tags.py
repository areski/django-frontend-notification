#
# Common Notification License
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#


from django.template.defaultfilters import register
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from common_notification.views import notice_count


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
        return _('New')
    else:
        return _('Read')


@register.simple_tag(name='get_notice_count')
def get_notice_count(request):
    """tag to display notice count"""
    return notice_count(request)
