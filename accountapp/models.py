from django.contrib.auth.models import AbstractUser
from django.db import models
from stdimage.models import StdImageField
from stdimage.validators import MinSizeValidator, MaxSizeValidator
from django.core.exceptions import ValidationError


def validate_avatar_size(value):
    """ restrict the size of avatar uploaded """
    filesize = value.size
    limit_kb = 50
    if filesize > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
    # limit_mb = 8
    # if file_size > limit_mb * 1024 * 1024:
    # raise ValidationError("Max size of file is %s MB" % limit_mb)
    else:
        return value


def avatar_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/img/avatars/username.png
    return 'img/avatars/{0}.png'.format(instance.username, )


class MyUser(AbstractUser):
    """ Model to store all auth users """
    # add custom fiels for default User profile HERE
    avatar = StdImageField(
        upload_to=avatar_directory_path,  # path/to/imgs
        variations={'thumbnail': (150, 150, True)},  # resize
        validators=[
            validate_avatar_size,  # size
            MinSizeValidator(150, 150),  # min dimension
            MaxSizeValidator(300, 300)],  # max dimension
        delete_orphans=True,  # delete orphaned files
        blank=True,)
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
