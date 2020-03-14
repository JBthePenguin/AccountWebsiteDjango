from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MyLoginView, dashboard, redirect_dasboard_user


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', redirect_dasboard_user),
    path('dashboard/<str:username>/', dashboard, name='dashboard'),
]
