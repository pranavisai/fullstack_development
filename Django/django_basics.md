Django is a free and open-source web framework.

A Django project is a collection of applications and configurations that when combined together will make up the full web application.

It is important to use venv(virtual environment) as it allows you to have a virtual environment of Python and packages on a computer.

The virtual environment contains the newer version of the package. In Anaconda the virtual environment handler is included.

To create a virtual environment with conda:
``` conda create --name myEnv django ```

activate environment: ``` source activate myEnv ```

Anything installed with pip or conda will be only within that environment. So it is easier to create multiple virtual environments with different versions and packages.

To install Django ```conda install django```

Deactivate the environment: ``` conda deactivate environment ```

When Django is installed it also installs a command line called -> django-admin 

To create a project we need to use the command: ```django-admin startproject projectname```

### Explanation of the files created accordingly:

1. __init__.py -> This is a blank Python script that lets Python know that this directory can be treated as a package.
2. settings.py -> This is where all the settings of the project are stored.
3. urls.py -> This is a Python script that stores all the URL patterns for the project. That is different pages of the web application.
4. wsgi.py -> This Python script acts as a web server gateway interface. It will help us deploy the app to production.
5. manage.py -> This is a Python script that will associate with many commands as the app builds on.
6. asgi.py -> ASGI is asynchronous, handling multiple requests concurrently without blocking other requests.

To run the project ```python manage.py runserver```
This will provide a local URL with the port number on which the Django application is running.

#### Migrations:

Migrations allow us to move databases from one design to another. This is also reversible.

### Building an application:

Create an application using: ```python manage.py startapp appname```

### Explanation of the files created accordingly:

1. __init__.py -> This is a blank Python script that lets Python know that this directory can be treated as a package.
2. admin.py -> To register models which Django can then use with Django's admin interface.
3. apps.py -> For placing application-specific configurations.
4. models.py -> Store the application's data models. Specify the entities and relationships between data.
5. Test.py -> To store the test functions used to test code.
6. Views.py -> To store functions that handle requests and return responses.
7. Migrations folder -> This directory stores database-specific information as it relates to the models.

To add the created application to the Django project:
Go to settings.py in the project folder(created before the app folder) and in the __INSTALLED_APPS__ array add the application: ```appname```

It is not possible to use ```django.conf.urls``` anymore as it has been removed from the recent versions of Django. Instead, the path or re_path is being used.

To run the project use: ```python manage.py runserver```


### URL Mapping

1. The include() function allows us to look for a match with regular expressions and link back to our application's own urls.py file.
2. We need to add this manually in the urls.py file.
```
   from django.conf.urls import include
   urlpatters = [...
  path('yourappname/', include('yourappname.urls')),
  ...]
```
This pattern is helping us find the pattern: www.domainname.com/yourappname/..
3. When the pattern is matched the include() function tells Django to look at the urls.py file instead of the yourappname folder.

### Django templates:

1. Templates will contain the static parts of an HTML page.
2. The template tags have their own special syntax.
3. This allows you to inject dynamic content that the Django app's views will produce, affecting the final HTML.
4. Next, let Django know of the templates by editing the DIR Key inside the templates dictionary in the settings.py file.
5. To prevent the hard coded path in the dictionary we use Python's module to dynamically generate the correct file path strings.
6. ```
   from pathlib import Path
   print(__file__) \\ used to print out the whole path of the file.```
7. The template tags are a mix of HTML and Python.
8. To inject content we will use the render() function and place it into our original index() function inside our views.py file.
9. To give a directory in settings.py. We must also provide the directory name in the TEMPLATES array. In the existing DIRS empty array do this:
``` "DIRS": [BASE_DIR / "templates"],```
10. To give in views.py in the app folder for the template tag: ```
def index(request):
    my_dict = {'insert_me': "Hello! I am from views.py!",}
    return render(request, 'index.html', my_dict) ```

### static files

1. First create a folder in the main directory named static. Then you can add css or images within the respective folder of this.
2. After that in the settings.py folder create a directory for ```STATIC_DIR = BASE_DIR / "static"```.
3. Make sure the ```"django.contrib.staticfiles",``` is present in the INSTALL_APPS array.
4. In the same file, bottom there will be a ```STATIC_URL = "static/"```, if not create and add the STATIC_DIR as follows: ```STATICFILES_DIRS = [STATIC_DIR,]```.
5. Example of how the tags should be added to the HTML page is as below. 
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django Image</title>
    <link rel="stylesheet" href="{% static 'css/mystyle.css' %}"/>
</head>
<body>
    <h1>This is a picture of Django</h1>
    {% load static %}
    <img src="{% static 'images/djangoimage.jpg' %}" alt="Uh oh! Didn't show">
</body>
</html>
 ```

