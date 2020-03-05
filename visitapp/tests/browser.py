from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser(StaticLiveServerTestCase):
    """ A web browser selenium """

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
        """ init wait """
        self.wait = WebDriverWait(self.selenium, 10)
