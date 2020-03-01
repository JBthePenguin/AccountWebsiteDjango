from django.shortcuts import render

DEFAULT_CONTEXT = {
    'title_site': 'Simple Django Website',
    'nav_brand': 'Simple Base',
}


def index(request):
    # return the home page
    context = {
        'home_in_nav': 'active',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/index.html', context)
