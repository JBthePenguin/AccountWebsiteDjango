from django.shortcuts import render

DEFAULT_CONTEXT = {
    'title_site': 'Simple Website',
    'nav_brand': 'Simple Base',
}


def home(request):
    # return the home page
    context = {
        'page_title': 'Home',
        'home_in_nav': 'active',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/home.html', context)


def page_one(request):
    # return the page one
    context = {
        'page_title': 'Page 1',
        'page_one_in_nav': 'active',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/page_one.html', context)


def page_two(request):
    # return the page two
    context = {
        'page_title': 'Page 2',
        'page_two_in_nav': 'active',
    }
    context.update(DEFAULT_CONTEXT)
    return render(request, 'visitapp/page_two.html', context)
