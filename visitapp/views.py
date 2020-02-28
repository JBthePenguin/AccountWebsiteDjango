from django.shortcuts import render


def index(request):
    # return the home page
    return render(request, 'visitapp/index.html')
