from django.shortcuts import render
from django.contrib.auth.views import LoginView
from visitapp.views import DEFAULT_CONTEXT


class MyLoginView(LoginView):
    extra_context = {
        'page_title': 'Login',
        'login_in_nav': 'active',
    }
    extra_context.update(DEFAULT_CONTEXT)


def dashboard(request):
    # return the dashboard for a user authenticated
    # context = {
    #     'page_title': 'Home',
    #     'home_in_nav': 'active',
    # }
    # context.update(DEFAULT_CONTEXT)
    return render(request, 'accountapp/dashboard.html', DEFAULT_CONTEXT)
