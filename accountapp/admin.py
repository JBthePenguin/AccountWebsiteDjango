from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from django.utils.translation import ugettext_lazy as _


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    """ Model for auth User in admin site """
    # lists to display, filter and search User
    list_display = (
        'username', 'first_name', 'last_name', 'email',
        'phone', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'groups', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    # add form configs with email required
    add_form_template = 'accountapp/admin_add_form.html'

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
            # change form page
            obj = MyUser.objects.get(pk=object_id)
            title = 'Change '
            if obj.is_staff:
                if obj.is_superuser:
                    title += 'Super User'
                else:
                    title += 'Staff User'
            else:
                title += 'Non Staff User'
        else:
            # add form page
            title = 'Add a User'
        extra_context = {'title': title}
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
        # default perm_fields
        perm_fields = ('is_active', 'groups', 'is_superuser')
        return [
            (None, {
                'fields': ('username', 'password')}),
            (_('Personal info'), {
                'fields': (
                    'first_name', 'last_name', 'email',
                    'phone', 'date_of_birth')}),
            (_(''.join([
                'Date joined: ', obj.date_joined.strftime('%Y-%m-%d')])), {
                'fields': ()}),
            (_(''.join([
                'Last Login: ', last_login])), {
                'fields': ()}),
            (_('Permissions'), {
                'fields': perm_fields}),
            # uncomment to allow change last_login and date_joined
            # (_('Important dates'), {'fields': ('last_login', 'date_joined')})
        ]
