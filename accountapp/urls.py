from django.urls import path
from .views import MyLoginView, dashboard


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]
