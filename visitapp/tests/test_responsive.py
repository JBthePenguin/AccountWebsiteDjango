# Tests with Selenium for responsive design
from django.urls import reverse
from .browser import Browser
from time import sleep


XS_SIZE = (360, 640, 'xs')
S_SIZE = (640, 850, 's')
M_SIZE = (768, 1024, 'm')
L_SIZE = (1024, 768, 'l')
XL_SIZE = (1280, 950, 'xl')

SIZES = [XS_SIZE, S_SIZE, M_SIZE, L_SIZE, XL_SIZE]

DIR = 'visitapp/tests/img_responsive/'


class ResponsiveTests(Browser):
    """ class test for responsive design
    - images to look things on the page """
    def test_navbar_responsive(self):
        """ images to look navbar -> visitapp/tests/img_responsive/navbar """
        out_dir = '%snavbar/' % DIR
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        # large screen
        self.selenium.set_window_size(L_SIZE[0], L_SIZE[1])
        self.selenium.save_screenshot('%sl.png' % out_dir)
        # small screen
        self.selenium.set_window_size(S_SIZE[0], S_SIZE[1])
        self.selenium.save_screenshot('%ss_without_links.png' % out_dir)
        button = self.selenium.find_element_by_class_name('navbar-toggler')
        button.click()
        sleep(1)
        self.selenium.save_screenshot('%ss_with_links.png' % out_dir)
        button.click()

    def take_screenshots(self, size, out_dir):
        """ set the window size and save 2 screenshots of the browser
        - up and down scroll"""
        self.selenium.set_window_size(size[0], size[1])
        self.selenium.save_screenshot('%s%s_up.png' % (out_dir, size[2]))
        self.selenium.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")
        self.selenium.save_screenshot('%s%s_down.png' % (out_dir, size[2]))
        self.selenium.execute_script(
            "window.scrollTo(0, 0)")

    def test_home_responsive(self):
        """ imgs to look home page -> visitapp/tests/img_responsive/home """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        out_dir = '%shome/' % DIR
        for size in SIZES:
            self.take_screenshots(size, out_dir)

    def test_page_one_responsive(self):
        """ imgs to look page one -> visitapp/tests/img_responsive/page_one """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('page one')))
        out_dir = '%spage_one/' % DIR
        for size in SIZES:
            self.take_screenshots(size, out_dir)

    def test_page_two_responsive(self):
        """ imgs to look page two -> visitapp/tests/img_responsive/page_two """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('page two')))
        out_dir = '%spage_two/' % DIR
        for size in SIZES:
            self.take_screenshots(size, out_dir)
