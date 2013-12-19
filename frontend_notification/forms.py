from django import forms
from frontend_notification.constants import NOTICE_TYPE


class NotificationForm(forms.Form):
    """
    Notification Form
    """
    notification_list = forms.ChoiceField(required=True, choices=list(NOTICE_TYPE))

    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
        self.fields['notification_list'].widget.attrs['class'] = "form-control"
        self.fields['notification_list'].widget.attrs['onchange'] = 'this.form.submit();'
