from django.urls import reverse
from visitapp.tests.test_templates import TemplatesContent
from ..models import MyUser


class AccountTemplatesTests(TemplatesContent):
    """ class test for templates
    - titles (site, navbar, page)
    - links
    - content """

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        MyUser.objects.create_user(**self.credentials)

    def login_with_form(self):
        """ login to account with form """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('login')))
        form = self.selenium.find_element_by_tag_name('form')
        form.find_element_by_id('id_username').send_keys(
            self.credentials['username'])
        form.find_element_by_id('id_password').send_keys(
            self.credentials['password'])
        button = form.find_element_by_tag_name('button')
        self.link_url(button, 'Dashboard', reverse('dashboard'))

    def test_base(self):
        """ test the base template
        - titles site """
        titles = [('login', 'Login'), ]
        self.site_titles(titles)
        self.login_with_form()
        titles = [('dashboard', 'Dashboard'), ]
        self.site_titles(titles)
