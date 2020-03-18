# Tests for all views in acountapp
from visitapp.tests.test_views import ViewsUrlTemplate
from ..models import MyUser


class AccountViewsTests(ViewsUrlTemplate):
    """ class test for views in visitapp """
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        MyUser.objects.create_user(**self.credentials)

    def test_login_logout_view(self):
        """ tests for login view
        - url and name
        - templates used
        - login / logout authentification and redirect"""
        self.url_name('/account/login/', 'login')
        templates = [
            'visitapp/base.html',
            'visitapp/navbar.html',
            'registration/login.html',
            'visitapp/footer.html', ]
        self.status_templates('/account/login/', templates)
        # connect test and redirect
        response = self.client.post(
            '/account/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.redirect_chain[0][0], '/account/dashboard/')
        # user authenticated redirect if he get login
        response = self.client.get(
            '/account/login/', follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/account/dashboard/')
        # disconnect test and redirect
        self.url_name('/account/logout/', 'logout')
        response = self.client.get('/account/logout/', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertEqual(response.redirect_chain[0][0], '/')

    def test_dashboard_view(self):
        """ tests for dashboard view
        - url and name
        - templates used """
        self.client.post('/account/login/', self.credentials, follow=True)
        self.url_name('/account/dashboard/', 'dashboard')
        templates = [
            'visitapp/base.html',
            'visitapp/navbar.html',
            'accountapp/usernavbar.html',
            'accountapp/dashboard.html',
            'visitapp/footer.html', ]
        self.status_templates('/account/dashboard/', templates)
