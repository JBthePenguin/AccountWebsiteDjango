from django.urls import path
from .views import home, page_one, page_two


urlpatterns = [
    path('', home, name='home'),
    path('page-1/', page_one, name='page one'),
    path('page-2/', page_two, name='page two'),
]
