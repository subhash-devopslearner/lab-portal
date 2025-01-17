# Create Django template

Upto now, I have created **home** app in Django project and configured the app to behave as homepage.  
On the homepage, I can only see a HTML Response of **Welcome to Lab Portal** message.  

Now I will create HTML pages for for the **home** app.  

## Create HTML template structure for app

In **home** app folder create a **templates** folder as shown below  

`mkdir templates/home`  

## Create a BASE template 

In my **home** app there will be many HTML pages to serve different fuctionalities.  
To serve the header, navigation, footer and other stuff with all HTML pages, I need a BASE template.  

So I will create a **base.html** file in **templates/home** folder with contents as below  

```
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">    
    <title> {% block title %} {% endblock %} </title>
    <link href="{% static 'home/css/bootstrap.css' %}">
  </head>  
  <body>
    {% block content %}

    {% endblock %}
  </body>
</html>
```

## Create HTML pages 

Now I can create HTML pages for my app.  
First I create a **home.html** as index page of **home** app.  

I will extend my **base.html** content with my **home.html** as below  

```
{% extends 'home/base.html' %}
{% block title %} Lab Portal | Home {% endblock %}

{% block content %}
<h1>Welcome to Lab Portal</h1>
{% endblock %}
```

With **extends** tag used above I can extend the contents of **base.html** with **home.html**.  

Now I can put all my headers, navigations and footer in **base.html** and I don't need to repeat it on other HTML pages.  

I have to just put my HTML contents inside `{% block content %} content {% endblock %}` block.  

## Render HTML pages in views

Now I have to render my **home.html** file as **home** app index page.  
So I will edit **views.py** in **home** folder as below  

```
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
```

## Check Django app with HTML template

To check the templates are accessible, start Django delevopment server and access the link http://127.0.0.1:8000.  