# How to keep secrets in Django

In Django, there are some settings, that should be kept secure and should not push to code repositories directly.

You should load following variable values from **.env** (environment) file.  
1. **SECRET_KEY**
2. **DEBUG**
3. **ALLOWED_HOSTS**

## How to put variable values in **.env** file

1. create a file .env in the base folder (where .manage.py file present).  
2. Install python-dotenv package - `pip install python-dotenv`.    
3. Add this file to requirements.txt - `pip freeze > requirements.txt`.    
4. Add entries for SECRET_KEY, DEBUG and ALLOWED_HOSTS in **.env** file.  

```
DJANGO_SECRET_KEY='secret-key-generated'
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS='host1,host2,host3'
```

## What is secret_key

The `SECRET_KEY` in Django is a critical setting used for various security-related operations.  
It is used to provide cryptographic signing, and should be set to a unique, unpredictable value.   

1. **Session Management**: It is used to sign session cookies.
2. **Password Reset Tokens**: It is used to generate tokens for password reset functionality.
3. **CSRF Protection**: It is used to sign CSRF tokens.
4. **Message Signing**: It is used to sign messages in Django's messaging framework.  

### Generate secret_key in Django

Start python shell - `python manage.py shell`  

At python shell, run the following commands -  

`from django.core.management.utils import get_random_secret_key`

`print(get_random_secret_key())`  

Copy the generated string to use as your `SECRET_KEY`.    

### Setting the `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS`

You should set the `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS` in your **.env** file and set it in `settings.py` file to read from `.env` file.    

#### settings.py file
```python
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-$a@_t*$x^162%zd6$r6$2q=g50*ekhpox(_!jk-l*00kaf$*nf')

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')
```

Don't forget to add entry for **.env** file in **.gitignore**.  
In this way you can use the Django for development and production without changing any setting.  