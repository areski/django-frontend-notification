from django_lets_go.utils import BaseAuthenticatedClient
from frontend_notification.views import user_notification,\
    notification_del_read, update_notification


class NotificationCustomerView(BaseAuthenticatedClient):
    """Test Function to check Notification pages"""

    fixtures = ['auth_user.json', 'notification.json']

    def test_user_notification(self):
        """Test Function to check User settings"""
        response = self.client.get(
            '/user_notification/?notification=mark_read_all', {})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'frontend/frontend_notification/user_notification.html')
        request = self.factory.get('/user_notification/')
        request.user = self.user
        request.session = {}
        response = user_notification(request)
        self.assertEqual(response.status_code, 200)

    def test_notification_del_read(self):
        """Test Function to check delete notification"""
        request = self.factory.post(
            '/user_notification/del/1/',
            {'mark_read': 'false'})
        request.user = self.user
        request.session = {}
        response = notification_del_read(request, 1)
        self.assertEqual(response.status_code, 302)

        request = self.factory.post(
            '/user_notification/del/2/',
            {'select': '1,2'})
        request.user = self.user
        request.session = {}
        response = notification_del_read(request, 2)
        self.assertEqual(response.status_code, 302)

        request = self.factory.post(
            '/user_notification/del/',
            {'select': '1', 'mark_read': 'true'})
        request.user = self.user
        request.session = {}
        response = notification_del_read(request, 0)
        self.assertEqual(response.status_code, 302)

    def test_update_notification(self):
        """Test Function to check update notice status"""
        request = self.factory.post(
            '/user_notification/1/',
            {'select': '1'})
        request.user = self.user
        request.session = {}
        response = update_notification(1)
        self.assertEqual(response.status_code, 302)
