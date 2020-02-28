from django.shortcuts import render


def index(request):
    # return the home page
    context = {
        'home_in_navabar': 'active',
    }
    return render(request, 'visitapp/index.html', context)
