from django.urls import reverse
from visitapp.tests.test_templates import TemplatesContent
from ..models import MyUser


class AccountTemplatesTests(TemplatesContent):
    """ class test for templates in account app
    - titles (site, navbar, page)
    - links
    - content """

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret', }
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

    def logout_with_navbutton(self):
        """ click on logout button in navbar """
        user_navbar = self.selenium.find_element_by_class_name('navbar')
        navbarnavs = user_navbar.find_elements_by_class_name('navbar-nav')
        nav_items = navbarnavs[-1].find_elements_by_class_name('nav-item')
        logout_link = nav_items[-1].find_element_by_class_name('nav-link')
        self.link_url(logout_link, 'Home', reverse('home'))

    def test_base(self):
        """ test the base template
        - titles site """
        titles = [('login', 'Login'), ]
        self.site_titles(titles)
        self.login_with_form()
        titles = [('dashboard', 'Dashboard'), ]
        self.site_titles(titles)
        self.logout_with_navbutton()

    def test_usernavbar(self):
        """ test the user navbar template
        - dashboard link
        - logout """
        self.login_with_form()
        # get home page
        user_navbar = self.selenium.find_element_by_class_name('navbar')
        home_link = user_navbar.find_element_by_link_text('Home')
        self.link_url(home_link, 'Home', reverse('home'))
        # dashboard link active
        user_navbar = self.selenium.find_element_by_class_name('navbar')
        dashboard_link = user_navbar.find_element_by_link_text(
            self.credentials['username'])
        self.link_url(dashboard_link, 'Dashboard', reverse('dashboard'))
        user_navbar = self.selenium.find_element_by_class_name('navbar')
        dashboard_link = user_navbar.find_element_by_link_text(
            self.credentials['username'])
        nav_item = dashboard_link.find_element_by_xpath("..")
        self.assertIn('active', nav_item.get_attribute('class'))
        # logout
        self.logout_with_navbutton()

    def test_dashboard(self):
        """ test the dasboard template
        - dashboard link
        - logout """
        self.login_with_form()
        self.header_content(self.credentials['username'])
        self.tag_number('div', 10)
        self.logout_with_navbutton()
