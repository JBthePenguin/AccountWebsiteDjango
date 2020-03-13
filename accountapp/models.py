from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """ Model to store all auth users """
    # add custom fiels for default User profile HERE
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = "My User"
        verbose_name_plural = "My Users"

# it's possible to update an attribute or add a constaint
# to existing fields on MyUser HERE
# MyUser._meta.get_field('email').blank = False
# MyUser._meta.get_field('email')._unique = True
