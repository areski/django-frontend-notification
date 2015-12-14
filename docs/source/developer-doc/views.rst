.. _views:

Django-Frontend-Notification Views
==================================


.. _user-notification-view:

:class:`user_notification`
--------------------------

  User Detail change on Customer UI

      **Attributes**:

          * ``form`` - UserChangeDetailForm, UserChangeDetailExtendForm,
                          PasswordChangeForm, CheckPhoneNumberForm
          * ``template`` - 'frontend/frontend_notification/user_notification.html'

      **Logic Description**:

          * User is able to change his/her detail.


.. _notification-del-read-view:

:class:`notification_del_read`
------------------------------

  Delete notification for the logged in user

      **Attributes**:

          * ``object_id`` - Selected notification object
          * ``object_list`` - Selected notification objects

      **Logic Description**:

          * Delete/Mark as Read the selected notification


.. _update-notification-view:

:class:`update_notification`
----------------------------

  Notification Status (e.g. read/unread) can be changed from
      customer interface


.. _frontend_send_notification-view:

:class:`frontend_send_notification`
-----------------------------------

  User Notification (e.g. start | stop | pause | abort |
      contact/campaign limit) needs to be saved.
      It is a common function for the admin and customer UI's

      **Attributes**:

          * ``pk`` - primary key of the campaign record
          * ``status`` - get label for notifications




.. _frontend-notification-status-view:

:class:`frontend_notification_status`
-------------------------------------

  Notification Status (e.g. read/unread) need to be change.
      It is a common function for admin and customer UI

      **Attributes**:

          * ``pk`` - primary key of notice record

      **Logic Description**:

          * Selected Notification's status need to be changed.
            Changed status can be read or unread.


.. _notice-count:

:class:`notice_count`
---------------------

  Get count of logged in user's notifications

