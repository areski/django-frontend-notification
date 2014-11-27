from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.utils.translation import ugettext_lazy as _
from notification import models as notification
from frontend_notification.constants import NOTICE_TYPE
from frontend_notification.forms import NotificationForm
from django_lets_go.common_functions import get_pagination_vars


def frontend_notification_status(id):
    """Notification Status (e.g. seen/unseen) need to be change.
    It is a common function for admin and customer UI

    **Attributes**:

        * ``pk`` - primary key of notice record

    **Logic Description**:

        * Selected Notification's status need to be changed.
          Changed status can be seen or unseen.
    """
    notice = notification.Notice.objects.get(pk=id)
    if notice.unseen == 1:
        notice.unseen = 0
    else:
        notice.unseen = 1
    notice.save()
    return True


def frontend_send_notification(request, status, recipient=None):
    """User Notification (e.g. start | stop | pause | abort |
    contact/campaign limit) needs to be saved.
    It is a common function for the admin and customer UI's

    **Attributes**:

        * ``pk`` - primary key of the campaign record
        * ``status`` - get label for notifications
    """
    if not recipient:
        recipient = request.user
        sender = User.objects.get(username=recipient)
    else:
        if request.user.is_anonymous():
            sender = User.objects.get(is_superuser=1, username=recipient)
        else:
            sender = request.user

    if notification:
        note_label = notification.NoticeType.objects.get(default=status)
        notification.send_now([recipient], note_label.label, {"from_user": request.user}, sender=sender)
    return True


@login_required
def notification_list(request):
    """User Detail change on Customer UI

    **Attributes**:

        * ``form`` - UserChangeDetailForm, UserChangeDetailExtendForm,
                        PasswordChangeForm, CheckPhoneNumberForm
        * ``template`` - 'frontend/frontend_notification/user_notification.html'

    **Logic Description**:

        * User is able to change his/her detail.
    """
    sort_col_field_list = ['message', 'notice_type', 'sender', 'added']
    pag_vars = get_pagination_vars(request, sort_col_field_list, default_sort_field='id')
    form = NotificationForm(request.POST or None, initial={'notification_list': NOTICE_TYPE.ALL})

    notification_list = NOTICE_TYPE.ALL
    post_var_with_page = 0
    if form.is_valid():
        request.session['session_notification_list'] = ''
        post_var_with_page = 1

        if request.POST.get('notification_list'):
            notification_list = request.POST.get('notification_list')
            request.session['session_notification_list'] = notification_list

    if request.GET.get('page') or request.GET.get('sort_by'):
        post_var_with_page = 1
        notification_list = request.session.get('session_notification_list')
        form = NotificationForm(initial={'notification_list': notification_list})

    if post_var_with_page == 0:
        # default
        # unset session var
        request.session['session_notification_list'] = ''

    kwargs = {}
    kwargs['sender'] = request.user
    if notification_list and notification_list != NOTICE_TYPE.ALL:
        kwargs['unseen'] = notification_list

    user_notification = notification.Notice.objects.filter(recipient=request.user)
    if kwargs:
        user_notification = user_notification.filter(**kwargs)

    all_user_notification = user_notification.order_by(pag_vars['sort_order'])
    user_notification = all_user_notification[pag_vars['start_page']:pag_vars['end_page']]
    user_notification_count = all_user_notification.count()

    msg_note = ''
    if request.GET.get('msg_note') == 'true':
        msg_note = request.session['msg_note']

    # Mark all notification as read
    if request.GET.get('notification') == 'mark_read_all':
        notification_list = notification.Notice.objects.filter(unseen=1, recipient=request.user)
        notification_list.update(unseen=0)
        msg_note = _('all notifications are marked as read.')

    data = {
        'form': form,
        'msg_note': msg_note,
        'all_user_notification': all_user_notification,
        'user_notification': user_notification,
        'user_notification_count': user_notification_count,
        'col_name_with_order': pag_vars['col_name_with_order'],
    }
    return render_to_response(
        'frontend/frontend_notification/user_notification.html', data, context_instance=RequestContext(request))


@login_required
def notification_del_read(request, object_id):
    """Delete notification for the logged in user

    **Attributes**:

        * ``object_id`` - Selected notification object
        * ``object_list`` - Selected notification objects

    **Logic Description**:

        * Delete/Mark as Read the selected notification
    """
    try:
        # When object_id is not 0
        notification_obj = notification.Notice.objects.get(pk=object_id)
        # Delete/Read notification
        if object_id:
            if request.POST.get('mark_read') == 'false':
                request.session["msg_note"] = _('"%(name)s" is deleted.') % {'name': notification_obj.notice_type}
                notification_obj.delete()
            else:
                request.session["msg_note"] = _('"%(name)s" is marked as read.') % \
                    {'name': notification_obj.notice_type}
                notification_obj.update(unseen=0)

            return HttpResponseRedirect('/user_notification/?msg_note=true')
    except:
        # When object_id is 0 (Multiple records delete/mark as read)
        values = request.POST.getlist('select')
        values = ", ".join(["%s" % el for el in values])
        notification_list = notification.Notice.objects.extra(where=['id IN (%s)' % values])
        if request.POST.get('mark_read') == 'false':
            request.session["msg_note"] = _('%(count)s notification(s) are deleted.') % \
                {'count': notification_list.count()}
            notification_list.delete()
        else:
            request.session["msg_note"] = _('%(count)s notification(s) are marked as read.') % \
                {'count': notification_list.count()}
            notification_list.update(unseen=0)
        return HttpResponseRedirect('/user_notification/?msg_note=true')


@login_required
def update_notification(request, id):
    """Notification Status (e.g. seen/unseen) can be changed from
    customer interface"""
    frontend_notification_status(id)
    return HttpResponseRedirect('/user_notification/')
