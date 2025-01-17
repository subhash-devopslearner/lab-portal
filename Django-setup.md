# Install Django and Configure

Hi, here I am going to make Django based project for computer lab management.  

I amd using Ubuntu 22.04 as my development system.  

Django is an opensource web developement framework of Python programming language.  

## Create Python virtual environment for Django

1. `mkdir lab-portal`  
2. `python3 -m venv myprojectenv`
3. `source myprojectenv/bin/activate`

Using command 1, I have a created a folder **lab-portal** to hold my Django project.  
Using command 2, I have created **Python virtual environment** in **lab-portal** folder using `venv` module.  
Using command 3, I have actiavted **Python virtual environment**.  

After activating **Python virtual environment**, you will see **(myprojectenv)** text is added to the start of bash command line.

Add the **myprojectenv/** entry in **.gitignore** file of your project, that will make sure that your **Python virtual environment** will not be copied to your **GIT** project repository.  

## Upgrade pip version

`pip install pip --upgrade`

**PIP** is Python package manager and we will use it to install Django and other related stuff.  
Above command upgrades pip itself to the latest version available.  

1. `pip -V`
2. `which pip`
3. `which python`

Using command 1, verify pip version, it is version 24 now, while I am creating this project.  
Using command 2, verify pip location, it should point to the **lab-portal/myprojectenv/bin/pip** folder.  
Using command 2, verify Python location, it should point to the **lab-portal/myprojectenv/bin/python** folder.  

## Install Django 

`pip install django`  

Above command will install Django in our Python virtual environment.  
The current version of Django is version 5.1.4.  

## Create Django project  

`django-admin startproject labportal`

Make sure you are in **lab-portal** folder and hit above command to create a Django project **labportal** in current folder.  

## Create requirements.txt

`pip freeze > requirements.txt`  

Above command will copy Django and related package names with version in **requirements.txt** file.  

## Run Django site

`labportal/manage.py runserver`  

Run above command to start Django development server.  
If you see a line **Starting development server at http://127.0.0.1:8000/**, means Django is successfully installed and started.  

To access the Django server, open the link **http://127.0.0.1:8000** in any web browser, it will show a **Django** webpage.

Your Django installation is now ready and start devloping your project further.






