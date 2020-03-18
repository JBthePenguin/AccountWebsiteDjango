from django.forms.widgets import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    """ custom clearable input to display it on form error """
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
