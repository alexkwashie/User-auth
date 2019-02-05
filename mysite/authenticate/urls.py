from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login')
]