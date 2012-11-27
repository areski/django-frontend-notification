from django.conf.urls import patterns, include


urlpatterns = patterns('frontend_notification.views',
    # User notification for Customer UI
    (r'^user_notification/', 'user_notification'),
    (r'^user_notification/', include('notification.urls')),
    (r'^user_notification/del/(.+)/$', 'notification_del_read'),
    # Notification Status (seen/unseen) for customer UI
    (r'^update_notification/(\d*)/$', 'update_notification'),
)
