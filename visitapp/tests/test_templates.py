# Tests with Selenium for templates
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TemplatesTests(StaticLiveServerTestCase):
    """ class test for templates
    - titles (site, navbar, page)
    - links
    - content """

    @classmethod
    def setUpClass(cls):
        """ init a browser before test"""
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        """ close the browser after test """
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        """ Before tests """
        pass

    def test_base(self):
        """ test the base template
        - title site: title_site | page_title """
        # titles site
        titles = [
            ('home', 'Home'),
            ('page one', 'Page 1'),
            ('page two', 'Page 2'), ]
        for title in titles:
            self.selenium.get(
                '%s%s' % (self.live_server_url, reverse(title[0])))
            title_site = self.selenium.title
            self.assertEqual(title_site, 'Simple Website | %s' % (title[1]))

    def wait_page_loaded(self, title_page):
        """ wait page is loaded to continue test """
        wait = WebDriverWait(self.selenium, 10)
        wait.until(EC.title_contains(title_page))

    def link_url(self, link, title_page, link_url):
        """ test if a click on a link go to the correct url """
        link.click()
        self.wait_page_loaded(title_page)
        self.assertEqual(
            self.selenium.current_url,
            '%s%s' % (self.live_server_url, link_url))

    def test_navbar(self):
        """ test the navbar template
        - nav brand
        - nav links """
        # nav brand text
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        nav_brand = self.selenium.find_element_by_class_name('navbar-brand')
        self.assertEqual(nav_brand.text, "Simple Base")
        # number of nav links
        nav_links = self.selenium.find_elements_by_class_name("nav-link")
        self.assertEqual(len(nav_links), 3)
        # link text and url after click
        nav_links = [
            ('Page 1', 'Page 1', reverse('page one')),
            ('Simple Base', 'Home', reverse('home')),  # nav brand link
            ('Page 2', 'Page 2', reverse('page two')),
            ('Home', 'Home', reverse('home')), ]
        for nav_link in nav_links:
            nav_bar = self.selenium.find_element_by_class_name('navbar')
            link = nav_bar.find_element_by_link_text(nav_link[0])
            self.link_url(link, nav_link[1], nav_link[2])
