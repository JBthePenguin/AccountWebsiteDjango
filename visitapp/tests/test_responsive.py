# Tests with Selenium for responsive design
from django.urls import reverse
from .browser import Browser
from time import sleep

DIR = 'visitapp/tests/img_responsive/'


class ResponsiveScreenshots(Browser):
    """ class to take screenshots of a page """
    @classmethod
    def setUpClass(cls):
        """ init a browser before test"""
        super().setUpClass()
        size_xs = (360, 640, 'xs')
        size_s = (640, 850, 's')
        size_m = (768, 1024, 'm')
        size_l = (1024, 768, 'l')
        size_xl = (1280, 950, 'xl')
        cls.sizes = [size_xs, size_s, size_m, size_l, size_xl]

    def take_screenshots(self, out_dir):
        """ set the window size and save 2 screenshots of the browser
        for eah size up and down scroll"""
        for size in self.sizes:
            self.selenium.set_window_size(size[0], size[1])
            self.selenium.save_screenshot('%s%s_up.png' % (out_dir, size[2]))
            self.selenium.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            self.selenium.save_screenshot('%s%s_down.png' % (out_dir, size[2]))
            self.selenium.execute_script(
                "window.scrollTo(0, 0)")


class VisitappResponsiveTests(ResponsiveScreenshots):
    """ class test for responsive design in visitapp
    - images to look things on the page """
    def test_navbar_responsive(self):
        """ images to look navbar -> visitapp/tests/img_responsive/navbar """
        out_dir = '%snavbar/' % DIR
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
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
        button.click()

    def test_home_responsive(self):
        """ imgs to look home page -> visitapp/tests/img_responsive/home """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        out_dir = '%shome/' % DIR
        self.take_screenshots(out_dir)

    def test_page_one_responsive(self):
        """ imgs to look page one -> visitapp/tests/img_responsive/page_one """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('page one')))
        out_dir = '%spage_one/' % DIR
        self.take_screenshots(out_dir)

    def test_page_two_responsive(self):
        """ imgs to look page two -> visitapp/tests/img_responsive/page_two """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('page two')))
        out_dir = '%spage_two/' % DIR
        self.take_screenshots(out_dir)
