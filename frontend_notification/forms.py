from django import forms
from django.utils.translation import ugettext_lazy as _
from frontend_notification.constants import NOTICE_TYPE


class NotificationForm(forms.Form):
    """
    NotificationForm
    """
    notification_list = forms.ChoiceField(required=True, choices=list(NOTICE_TYPE))

    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)        
        self.fields['notification_list'].widget.attrs['class'] = "form-control"
        self.fields['notification_list'].widget.attrs['onchange'] = 'this.form.submit();'               