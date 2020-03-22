from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import MyRegistrationView, MyLoginView, dashboard


urlpatterns = [
    path(
        'register/', MyRegistrationView.as_view(),
        name='django_registration_register',),
    path('', include('django_registration.backends.activation.urls')),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
