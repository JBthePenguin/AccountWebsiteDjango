from django.forms.widgets import ClearableFileInput
from django_registration.forms import RegistrationFormUniqueEmail
from .models import MyUser


class MyRegistrationForm(RegistrationFormUniqueEmail):
    """ form that add unique contraint for email """
    class Meta(RegistrationFormUniqueEmail.Meta):
        model = MyUser

    def __init__(self, *args, **kwargs):
        super(MyRegistrationForm, self).__init__(*args, **kwargs)
        # change placeholder
        self.fields['username'].widget.attrs['placeholder'] = "YourUsername"
        self.fields['email'].widget.attrs[
            'placeholder'] = "youremail@address.com"
        self.fields['password1'].widget.attrs['placeholder'] = "YourPassword"
        self.fields['password2'].widget.attrs['placeholder'] = "SamePassword"
        # remove help text
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class MyClearableFileInput(ClearableFileInput):
    """ custom clearable input to display it on form error in admin site """
    template_name = "accountapp/clearable_file_input.html"

    def __init__(self, default_avatar):
        """ init the clear input
        with default avatar to use it in form error """
        super().__init__()
        self.default_avatar = default_avatar

    def format_value(self, value):
        """ return the default value for form error """
        try:
            getattr(value, 'url', False)
        except ValueError:
            pass
        else:
            if getattr(value, 'url', False) is False:
                # return the default value for form error
                if self.default_avatar.name == '':
                    return None
                return self.default_avatar
            # return the value for form
            return value

    def is_initial(self, value):
        """ return always true to display clear check button
        if file exist and False if not """
        if (value.name == '') or (self.default_avatar.name == ''):
            return False
        return True
