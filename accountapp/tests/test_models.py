from django.test import SimpleTestCase
from ..models import MyUser


class MyUserTests(SimpleTestCase):

    @classmethod
    def setUpClass(cls):
        cls.databases = '__all__'
        super(MyUserTests, cls).setUpClass()
        cls.user = MyUser(username='Joe', password='testpass')
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_str(self):
        """ Test method __str__()"""
        self.assertEqual(str(self.user), 'Joe')
