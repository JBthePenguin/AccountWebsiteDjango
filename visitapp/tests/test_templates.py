# Tests with Selenium for templates
from django.urls import reverse
from selenium.webdriver.support import expected_conditions as EC
from .browser import Browser


class TemplatesContent(Browser):
    """ Base class test for templates
    - title site
    - links
    - content """

    def site_titles(self, titles):
        """ test the site titles format
        - title_site | page_title """
        for title in titles:
            self.selenium.get(
                '%s%s' % (self.live_server_url, reverse(title[0])))
            title_site = self.selenium.title
            self.assertEqual(title_site, 'Account Website | %s' % (title[1]))

    def link_url(self, link, title_page, link_url):
        """ test if a click on a link go to the correct url """
        # click
        link.click()
        # wait page loaded
        self.wait.until(EC.title_contains(title_page))
        # assert link
        self.assertEqual(
            self.selenium.current_url,
            '%s%s' % (self.live_server_url, link_url))

    def link_new_tab(self, link, title_page, url):
        """ test if a click on a link open the correct url
        in a new tab, close it and switch to initial tab  """
        # click
        link.click()
        # wait new tab opened, get current tab and switch to the new
        self.wait.until(EC.number_of_windows_to_be(2))
        current_tab = self.selenium.current_window_handle
        self.selenium.switch_to_window(self.selenium.window_handles[1])
        self.wait.until(EC.title_contains(title_page))
        # verify url
        self.assertEqual(self.selenium.current_url, url)
        # close tab and switch to initial tab
        self.selenium.close()
        self.selenium.switch_to_window(current_tab)

    def header_content(self, title):
        """ test the header of a page
        - title
        - number of paragraph in main """
        header = self.selenium.find_element_by_tag_name('header')
        title_header = header.find_element_by_tag_name('h1')
        self.assertEqual(title, title_header.text)

    def tag_number(self, tag_name, num_tags):
        """ test the number of a tag in main """
        main = self.selenium.find_element_by_tag_name('main')
        tags_in_main = main.find_elements_by_tag_name(tag_name)
        self.assertEqual(num_tags, len(tags_in_main))


class VisitTemplatesTests(TemplatesContent):
    """ class test for templates
    - titles (site, navbar, page)
    - links
    - content """

    def test_base(self):
        """ test the base template
        - titles site """
        titles = [
            ('home', 'Home'),
            ('page one', 'Page 1'),
            ('page two', 'Page 2'), ]
        self.site_titles(titles)

    def test_navbar(self):
        """ test the navbar template
        - nav brand
        - nav links """
        # nav brand text
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        nav_brand = self.selenium.find_element_by_class_name('navbar-brand')
        self.assertEqual(nav_brand.text, "Account Base")
        # number of nav links
        nav_links = self.selenium.find_elements_by_class_name("nav-link")
        self.assertEqual(len(nav_links), 5)
        # link text and url after click
        nav_links = [
            ('Page 1', 'Page 1', reverse('page one')),
            ('Home', 'Home', reverse('home')),
            ('Page 2', 'Page 2', reverse('page two')),
            ('Login', 'Login', reverse('login')),
            ('Account Base', 'Home', reverse('home')), ]  # nav brand link
        i = 0
        for nav_link in nav_links:
            nav_bar = self.selenium.find_element_by_class_name('navbar')
            link = nav_bar.find_element_by_link_text(nav_link[0])
            self.link_url(link, nav_link[1], nav_link[2])
            # active link
            if nav_link[0] != 'Account Base':
                nav_bar = self.selenium.find_element_by_class_name('navbar')
                link = nav_bar.find_element_by_link_text(nav_link[0])
                nav_item = link.find_element_by_xpath("..")
                self.assertIn('active', nav_item.get_attribute('class'))
                # not active links
                if i == 0:
                    other_links = [nav_links[1], nav_links[2]]
                elif i == 1:
                    other_links = [nav_links[0], nav_links[2]]
                else:
                    other_links = [nav_links[0], nav_links[1]]
                for other_link in other_links:
                    other_link = nav_bar.find_element_by_link_text(
                        other_link[0])
                    other_nav_item = other_link.find_element_by_xpath("..")
                    self.assertNotIn(
                        'active',
                        other_nav_item.get_attribute('class'))
                i += 1

    def test_footer(self):
        """ test the footer template
        - social links url in new tab
        - mailto address """
        # social links
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        social_links = [
            (0, 'GitHub', 'https://github.com/JBthePenguin'),
            (1, 'Twitter', 'https://twitter.com/JBthePenguin'),
            # require to be connected at a linkedin account
            # (2, 'LinkedIn',
            #    'https://www.linkedin.com/in/jean-baptiste-labaty-a5b084155/'),
        ]
        for social_link in social_links:
            footer = self.selenium.find_element_by_tag_name('footer')
            social_icons = footer.find_elements_by_tag_name('a')
            self.link_new_tab(
                social_icons[social_link[0]], social_link[1], social_link[2])
        # mailto
        footer = self.selenium.find_element_by_tag_name('footer')
        social_icons = footer.find_elements_by_tag_name('a')
        mailto_icon = social_icons[3]
        email = mailto_icon.get_attribute("href")
        self.assertEqual(
            email.replace("mailto:", ""),
            'jbthepenguin@netcourrier.com')

    def test_home_template(self):
        """ test the home template
        - page content: title, n paragrah """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        self.header_content('Home page')
        self.tag_number('p', 3)

    def test_page_one_template(self):
        """ test the page one template
        - page content: title, n paragrah """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('page one')))
        self.header_content('Page one')
        self.tag_number('p', 1)

    def test_page_two_template(self):
        """ test the page two template
        - page content: title, n paragrah """
        self.selenium.get('%s%s' % (self.live_server_url, reverse('page two')))
        self.header_content('Page two')
        self.tag_number('p', 6)
