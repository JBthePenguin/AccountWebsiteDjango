from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from phone_field import PhoneField
from django.dispatch import receiver


class MyUser(AbstractUser):
    """ Model to store all auth users """
    # add custom fiels for default User profile HERE
    phone = PhoneField(blank=True, help_text='Contact phone number')
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['is_superuser', 'is_staff', 'username']
        verbose_name = "My User"
        verbose_name_plural = "My Users"

# it's possible to update an attribute or add a constaint
# to existing fields on MyUser HERE
# MyUser._meta.get_field('email').blank = False
# MyUser._meta.get_field('email')._unique = True


@receiver(models.signals.post_save, sender=MyUser)
def add_staff_to_group(sender, instance, created, **kwargs):
    """ Add automatically staff group on user
    if is staff or superuser after save """
    if (
            instance.is_staff or instance.is_superuser) and not (
            instance.groups.filter(name='staff user').exists()):
        # get staff user group or create it if not exist
        try:
            group = Group.objects.get(name='staff user')
        except Group.DoesNotExist:
            group = Group.objects.create(name='staff user')
            group.save()
        # add staff group on staff user include superuser
        instance.groups.add(group)


@receiver(models.signals.m2m_changed, sender=MyUser.groups.through)
def user_groups_changed_handler(sender, instance, action, **kwargs):
    """ Change automatically staff user status
    if staff group is removed or added on it """
    if (
            action == 'post_remove') and (instance.is_staff) and not (
            instance.groups.filter(name='staff user').exists()):
        instance.is_staff = False
        instance.save()
    if (
            action == 'post_add') and not (instance.is_staff) and (
            instance.groups.filter(name='staff user').exists()):
        instance.is_staff = True
        instance.save()
