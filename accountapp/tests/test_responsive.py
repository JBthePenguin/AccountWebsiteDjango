# Tests with Selenium for responsive design
from django.urls import reverse
from django.utils import timezone
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from visitapp.tests.test_responsive import ResponsiveScreenshots
from ..models import MyUser

DIR = 'accountapp/tests/img_responsive/'


class AccountappResponsiveTests(ResponsiveScreenshots):
    """ class test for responsive design in accountapp
    - images to look things on the page """
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@somewhere.com',
            'date_of_birth': '2000-01-01',
            'date_joined': timezone.now(),
            'last_login': timezone.now(), }
        MyUser.objects.create_user(**self.credentials)

    def login_with_form(self):
        """ login to account with form """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('login')))
        form = self.selenium.find_element_by_tag_name('form')
        form.find_element_by_id('id_username').send_keys(
            self.credentials['username'])
        form.find_element_by_id('id_password').send_keys(
            self.credentials['password'])
        form.find_element_by_tag_name('button').click()
        self.wait.until(EC.title_contains('Dashboard'))

    def logout_with_navbutton(self):
        """ click on logout button in navbar """
        user_navbar = self.selenium.find_element_by_class_name('navbar')
        navbarnavs = user_navbar.find_elements_by_class_name('navbar-nav')
        nav_items = navbarnavs[-1].find_elements_by_class_name('nav-item')
        nav_items[-1].find_element_by_class_name('nav-link').click()
        self.wait.until(EC.title_contains('Home'))

    def test_navbar_responsive(self):
        """ images to look usernavbar -> accountapp/tests/img_responsive/usernavbar """
        out_dir = '%susernavbar/' % DIR
        self.login_with_form()
        # large screen
        self.selenium.set_window_size(self.sizes[3][0], self.sizes[3][1])
        self.selenium.save_screenshot('%sl.png' % out_dir)
        # small screen
        self.selenium.set_window_size(self.sizes[1][0], self.sizes[1][1])
        self.selenium.save_screenshot('%ss_without_links.png' % out_dir)
        button = self.selenium.find_element_by_class_name('navbar-toggler')
        button.click()
        sleep(1)
        self.selenium.save_screenshot('%ss_with_links.png' % out_dir)
        self.logout_with_navbutton()

    def test_login_responsive(self):
        """ imgs to look login page -> accountapp/tests/img_responsive/login """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('login')))
        out_dir = '%slogin/' % DIR
        self.take_screenshots(out_dir)

    def test_dashboard_responsive(self):
        """ imgs to look dashboard -> accountapp/tests/img_responsive/dashboard """
        self.login_with_form()
        sleep(1)
        out_dir = '%sdashboard/' % DIR
        self.take_screenshots(out_dir)
        self.logout_with_navbutton()
