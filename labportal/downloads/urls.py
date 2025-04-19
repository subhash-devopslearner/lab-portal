# downloads/urls.py
from django.urls import path, re_path
from .views import list_downloads

urlpatterns = [
    re_path(r'^(?P<subpath>.*)$', list_downloads, name='list_downloads'),
]
