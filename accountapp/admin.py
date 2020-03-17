from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, MyImageField
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import ClearableFileInput


class MyClearableFileInput(ClearableFileInput):
    template_name = "admin/widgets/clearable_file_input.html"

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
                return self.default_avatar
            # return the value for form
            return value

    def is_initial(self, value):
        """ return always true to display clear check button
        if file exist and False if not """
        if value.name == '':
            return False
        return True


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    """ Model for auth User in admin site """
    # lists to display, filter and search User
    list_display = (
        'username', 'first_name', 'last_name', 'email', "avatar",
        'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'groups', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # add form custom template
    add_form_template = 'accountapp/admin_add_form.html'

    def has_view_permission(self, request, obj=None):
        """ allow staff to view user """
        return request.user.is_staff

    def has_add_permission(self, request, obj=None):
        """ allow staff to add user """
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        """ allow superuser to change all users and
        staff to change only him and non staff user """
        return (request.user.is_superuser or (
            obj and ((obj.id == request.user.id) or not (obj.is_staff)))) or (
            request.user.is_staff and obj is None)  # allow staff to add user

    def has_delete_permission(self, request, obj=None):
        """ allow superuser to delete all users and
        staff to delete only him and non staff user """
        return request.user.is_superuser or (
            obj and not obj.is_staff)

    def changelist_view(self, request, extra_context=None):
        """ override changelist_view to
        - change title """
        # title
        title = 'List of '
        if request.user.is_superuser:
            # superuser
            title += 'all Users'
        else:
            title += 'Non Staff User'
        extra_context = {'title': title}
        return super(MyUserAdmin, self).changelist_view(
            request, extra_context=extra_context)

    def changeform_view(
            self, request, object_id, form_url, extra_context=None):
        """ override changeform_view to
        - change title """
        if object_id is not None:
            obj = MyUser.objects.get(pk=object_id)
            # change form page
            title = 'Change '
            if obj.is_staff:
                if obj.is_superuser:
                    title += 'Super User'
                else:
                    title += 'Staff User'
            else:
                title += 'Non Staff User'
            # change form widget
            self.formfield_overrides = {
                MyImageField: {
                    'widget': MyClearableFileInput(obj.avatar)},
            }
        else:
            # add form page
            title = 'Add a User'
        extra_context = {'title': title}
        # self.form.Meta.widgets = {'avatar': CustomClearableFileInput}
        # self.form.Meta.widgets['avatar'] = CustomClearableFileInput
        return super(MyUserAdmin, self).changeform_view(
            request, object_id, form_url, extra_context=extra_context)

    def get_fieldsets(self, request, obj=None):
        """ returm fieldsets for add or change user form  """
        if not obj:
            # fields for add form
            default_fields = (
                'username', 'password1', 'password2')  # email if required
            if request.user.is_superuser:
                # field is_staff in add form
                default_fields += ('is_staff', 'is_superuser')
            return [
                (None, {
                    'classes': ('wide',),
                    'fields': default_fields}),
            ]
        # fields for change form
        # format last_login
        if obj.last_login is None:
            last_login = ""
        else:
            last_login = obj.last_login.strftime('%Y-%m-%d at %H:%M:%S')
        # default perm_fields for staff user
        perm_fields = ('is_active', 'groups')
        if request.user.is_superuser:
            # perm fields for superuser
            perm_fields += ('is_staff', 'user_permissions', 'is_superuser')
        return [
            (None, {
                'fields': ('avatar', 'username', 'password')}),
            (_('Personal info'), {
                'fields': (
                    'first_name', 'last_name', 'email', 'date_of_birth')}),
            (_('Permissions'), {
                'fields': perm_fields, }),
            (_(''.join([
                'Date joined: ', obj.date_joined.strftime('%Y-%m-%d')])), {
                'fields': ()}),
            (_(''.join([
                'Last Login: ', last_login])), {
                'fields': ()}),
            # uncomment to allow change last_login and date_joined
            # (_('Important dates'), {'fields': ('last_login', 'date_joined')})
        ]
