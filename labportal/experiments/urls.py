from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_experiments, name='home_experiments'),
    path('upload/', views.upload_experiment, name='upload_experiment'),    
]