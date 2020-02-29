from django.shortcuts import render


def index(request):
    # return the home page
    context = {
        'home_in_nav': 'active',
    }
    return render(request, 'visitapp/index.html', context)
