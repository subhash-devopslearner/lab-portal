# Access Static Files

Till now, I have created **home** app in **labportal** Django project and tested it's working.  

I want this app to be built using Bootstrap framework.  
I don't want to use the Bootstrap CDN links, but I will provide Bootstrap CSS and JS files as static.  
This will be local site and won't depend on internet to work.  

To use Bootstrap CSS and JS files as static, I need to do some settings in Django.

## Make static folder at app level

In **home** app folder create static folder in following hierarchy.

`mkdir home/static/home/css`  
`mkdir home/static/home/js`  
`mkdir home/static/home/img`  

## Copy Bootstrap CSS and JS files

To use Bootstrap locally, I need to download Bootstrap CSS and JS files and move them to folders created above.

`cp Downloads/bootstrap.css home/static/home/css`  
`cp Downloads/bootstrap.js home/static/home/js`  

## STATIC files settings

To make these **Bootstrap CSS and JS** files accessible, I need edit **labportal/settings.py** as shown below  

```
import os
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Base URL to serve static files
STATIC_URL = 'static/'

# The absolute path to the directory where static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Base URL to serve media files
MEDIA_URL = 'media/'

# The absolute path to the directory where media files will be collected
MEDIA_ROOT = 'media'
```

In addition to static files, I have also done setting for media files also.  

## URL setting 

In  order to access static files and media files by Django development server, I need to edit **labportal/urls.py** as shown below  

```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
These setting are not recommonded in production.  
In production, to serve static files and media files, I need to use webserver like NGINX, APACHE2 etc.  

## Collect static files

All static files used by all Django apps are collected at **static** folder in Django project folder by using following command  

`./manage.py collectstatic`  

Now you will see a **static** folder with two apps **admin** and **home** with folder like CSS, JS etc.  

## Check STATIC files access 

In order to check if these static files are accessible or not, I have start Django development server.  

Then browse to http://127.0.0.1:8000/static/home/css/bootstrap.css.  
If you see Bootstrap CSS file loaded in browser, then all settings are done properly.  



