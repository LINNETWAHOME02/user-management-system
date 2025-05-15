### User Management System - Backend

#### Project Purpose:

* ##### This is a simple user management system that performs all CRUD operations.
* ##### It implements the following features:
1. Create user(POST request)
2. Delete user(DELETE request)
3. Change user password(POST request)
4. Update user's details(fully with the PUT request, partially with the PATCH request)

* ##### Bonus features:
1. Validating database entries, through model-level validation for username and email in the User model in models.py, password validation through the ```AUTH_PASSWORD_VALIDATORS``` setting in settings.py
2. User login (POST request)
3. Display all users in database (GET request)
4. User logout(POST request)

* ##### Stack used is **Django**

* ##### Setup instructions:
1. Start 'New Project' on PyCharm and select Pure Python(or Django) as used in this set up, make sure the interpreter type selected is the Project venv to create a virtual environment upon project creation.
2. Once the new project is created, create a django project using the terminal, command: ```django-admin startproject 'project' .``` to create it in the current directory.
3. Create the application using ```python manage.py startapp 'user'```
4. Add the app to settings.py in ```INSTALLED_APPS```
5. Add the app urls to the projects urls.py
6. Install the rest framework on the terminal to handle api requests using ```pip install djangorestframework```, and add it to the settings.py ```INSTALLED_APPS``` 
7. Create user model in models.py and register it in the user application's admin
```
    from django.contrib import admin

    from user.models import *

    # Register your models here.
    admin.site.register(AppUser)
```
8. Create a user serializer in serializer.py, import the serializers module from rest framework ```from rest_framework import serializers``` and import user model
9. Create your views(apis) in views.py, import all views into urls.py ```from user import views``` and add them to the urlpatterns list