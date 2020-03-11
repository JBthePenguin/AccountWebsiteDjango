from django.shortcuts import render
from visitapp.views import DEFAULT_CONTEXT


def dashboard(request):
    # return the dashboard for a user authenticated
    # context = {
    #     'page_title': 'Home',
    #     'home_in_nav': 'active',
    # }
    # context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/home.html', DEFAULT_CONTEXT)
