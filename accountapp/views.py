from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django_registration.backends.activation.views import RegistrationView
from .forms import MyRegistrationForm
from visitapp.views import DEFAULT_CONTEXT


class MyRegistrationView(RegistrationView):
    form_class = MyRegistrationForm
    # template_name = 'registration/register.html'
    extra_context = {
        'page_title': 'Register',
        'register_in_nav': 'active',
    }
    extra_context.update(DEFAULT_CONTEXT)
    # email_subject_template = 'registration/activation_email_subject.txt'
    # email_body_template = 'registration/activation_email_body.txt'


class MyLoginView(LoginView):
    extra_context = {
        'page_title': 'Login',
        'login_in_nav': 'active',
    }
    extra_context.update(DEFAULT_CONTEXT)

    def get(self, request, *args, **kwargs):
        """ get login page """
        if self.request.user.is_authenticated:
            # redirect to dashboard if user is authentiated
            return redirect('dashboard')
        # custom authentication_form
        self.authentication_form = AuthenticationForm
        self.authentication_form.base_fields['username'].widget.attrs[
            'placeholder'] = "YourUsername"
        self.authentication_form.base_fields['password'].widget.attrs[
            'placeholder'] = "YourPassword"
        return super(MyLoginView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        """ for login sucesss redirect to dashboard/username """
        return reverse('dashboard')


@login_required
def dashboard(request):
    # return the dashboard for a user authenticated
    context = {
        'page_title': 'Dashboard',
        'user_in_nav': 'active',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'accountapp/dashboard.html', context)
