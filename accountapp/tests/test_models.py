from django.test import TestCase
from ..models import MyUser
from django.conf import settings
from django.core.files import File
from os import path


settings.MEDIA_URL += 'test/'
settings.MEDIA_ROOT += '/test/'


class MyUserModelTests(TestCase):
    """ class test for models in accountapp """
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        self.user = MyUser.objects.create_user(**self.credentials)

    def test_str(self):
        """ test method __str__()"""
        self.assertEqual(self.user.username, 'testuser')

    def upload_avatar(self, filename, commit=True):
        """ upload with save_form_data and save a new image file for avatar """
        avatar = open(settings.MEDIA_ROOT + filename, 'rb')
        self.user.avatar.field.save_form_data(self.user, File(avatar))
        if commit is True:
            self.user.save()
        avatar.close()

    def check_avatar_urls(self):
        """ test urls path is ok """
        self.assertEqual(
            settings.MEDIA_URL + 'accountapp/img/avatars/avatar{0}.png'.format(
                self.user.id, ),
            self.user.avatar.url)
        self.assertEqual(
            settings.MEDIA_URL + (
                'accountapp/img/avatars/avatar{0}.thumbnail.png'.format(
                    self.user.id, )),
            self.user.avatar.thumbnail.url)

    def check_avatar_files(self):
        """ test files uploaded """
        self.assertTrue(path.isfile(settings.BASE_DIR + self.user.avatar.url))
        self.assertTrue(
            path.isfile(settings.BASE_DIR + self.user.avatar.thumbnail.url))

    def test_avatar_field(self):
        """ test for image field avatar
        save upload and delete """
        # urls saved and uploaded files
        self.upload_avatar('accountapp/img/test150.png')
        self.check_avatar_urls()
        self.check_avatar_files()
        # sizes image
        self.assertEqual(self.user.avatar.width, self.user.avatar.height, 150)
        # new avatar uploaded
        self.upload_avatar('accountapp/img/test300.png')
        self.check_avatar_urls()
        self.check_avatar_files()
        # sizes of new avatar
        self.assertEqual(self.user.avatar.width, self.user.avatar.height, 300)
        # add to big size image > 50kb
        origin_avatar = self.user.avatar._file
        self.upload_avatar('accountapp/img/test500.png', commit=False)
        self.assertEqual(self.user.avatar.width, self.user.avatar.height, 300)
        # clear avatar
        self.user.avatar.field.save_form_data(self.user, origin_avatar)
        self.user.avatar.delete()


settings.MEDIA_URL.replace('test/', '')
settings.MEDIA_ROOT.replace('/test/', '')
