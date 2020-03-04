# SimpleTestCase for all views
from django.test import SimpleTestCase
from django.urls import reverse


class ViewsTests(SimpleTestCase):
    """ class test for views
    - url and name
    - templates used """

    def url_name(self, url, name):
        """ test if the name corresponding with the good url """
        self.assertEqual(url, reverse(name))

    def status_templates(self, url, templates):
        """ test the response's status and templates used """
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_home_view(self):
        """ tests for home view
        - url and name
        - templates used """
        self.url_name('/', 'home')
        templates = [
            'visitapp/base.html',
            'visitapp/navbar.html',
            'visitapp/home.html',
            'visitapp/footer.html', ]
        self.status_templates('/', templates)

    def test_page_one_view(self):
        """ tests for page_one view
        - url and name
        - templates used """
        self.url_name('/page-1/', 'page one')
        templates = [
            'visitapp/base.html',
            'visitapp/navbar.html',
            'visitapp/page_one.html',
            'visitapp/footer.html', ]
        self.status_templates('/page-1/', templates)

    def test_page_two_view(self):
        """ tests for page_two view
        - url and name
        - templates used """
        self.url_name('/page-2/', 'page two')
        templates = [
            'visitapp/base.html',
            'visitapp/navbar.html',
            'visitapp/page_two.html',
            'visitapp/footer.html', ]
        self.status_templates('/page-2/', templates)
