# Create First App

Here, I am going to create first Django app **home**, it will be homepage for **lab-portal**.  

## Create Django app 

`./manage.py startapp home`

To fire this command, you need to be in the folder where **manage.py** file is present.

This will create **home** app and a folder with name **home** on your base path.  

## Register Django app

Now you have to register newly created **home** app in **labportal/settings.py** file as shown below  

```
# Application definition

INSTALLED_APPS = [
    'home',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Add url for Django app at project level

Next, you have to give a url to access your app.  

As **home** app is going to be your homepage, then it should be accessed with your domain name root (e.g. http://mysite.com).  

To do so, you need to change **labportal/urls.py** file as shown below  

```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
```

## Add url for Django app at app level

After that, you need to create a **urls.py** file in your **home** app folder and edit it as shown below  

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
]
```

## Add view for Django app url

In Django app, an app url is mapped with a **view**.  

To create a view for **home** app edit the **home/views.py** file as shown below  

```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Lab Portal')
```

## Check Django app 

Up to this point, you have created an app, an url for the app and a view.  

Run the Django development server with following command  

`./manage.py runserver`

Browse the url http://127.0.0.1:8080/ and you will see **home** app is serving at this link.  

