# users/urls.py

from django.urls import path
from .views import register_student, login_view, custom_logout_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register_student, name='register'),
    path('login/', login_view, name='login'),    
    path('logout/', custom_logout_view, name='logout'),  # custom logout view
]
