Django is a free and open-source web framework.

A Django project is a collection of applications and configurations that when combined will make up the full web application.

It is important to use Venv (virtual environment) as it allows you to have a virtual environment of Python and packages on a computer.

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

Create an application using: ```django-admin startapp appname```

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
This pattern is helping us find the pattern: www.domainname.com/yourappname/...
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

### Static files

1. First create a folder in the main directory named static. Then you can add CSS or images within the respective folder of this.
2. In the settings.py folder create a directory for ```STATIC_DIR = BASE_DIR / "static"```.
3. Make sure the ```"django.contrib.staticfiles",``` is present in the INSTALL_APPS array.
4. In the same file, bottom there will be a ```STATIC_URL = "static/"```, if not create and add the STATIC_DIR as follows: ```STATICFILES_DIRS = [STATIC_DIR,]```.
5. An example of how the tags should be added to the HTML page is as below. 
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
6. Sometimes the CSS style sheet is cached and does not load the changes. In your browser use Ctrl + Shift + R to force reload without cache.

### Models

1. Models are used to incorporate a database into a Django Project.
2. Django comes equipped with SQLite.
3. In the settings.py file the ENGINE parameter can be edited for DATABASES.
4. A class structure is used inside the relevant applications models.py file.
5. ```django.db.models.Model``` is the built-in class used to make all the models subclasses of it.
6. Each attribute represents a field of the class similar to column names with constraints in SQL.
7. Example of a model class: 
```
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, models.DO_NOTHING)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
```
8. Django's ForeignKey requires an on_delete argument to specify the behavior when the referenced object is deleted. Some options are:
   1. models.CASCADE: Deletes the object containing the ForeignKey when the referenced object is deleted.
   2. models.PROTECT: Prevents deletion of the referenced object by raising a ProtectedError.
   3. models.SET_NULL: Sets the ForeignKey to NULL when the referenced object is deleted (requires null=True on the field).
   4. models.SET_DEFAULT: Sets the ForeignKey to its default value when the referenced object is deleted.
   5. models.SET(): Sets the ForeignKey to the value passed to SET() when the referenced object is deleted.
   6. models.DO_NOTHING: Does nothing when the referenced object is deleted.
9. After models are set up the database migration is done.
10. Database migration command: ```python manage.py migrate```
11. To register the changes to the app: ```python manage.py makemigrations yourappname```
12. Run the ```python manage.py migrate``` again.
13. Open the Python shell to run and check the DB. Use command ```python manage.py shell```
14. In the shell give the command: ```from yourappname.models import yourclassname```, to check once type: ```print(yourclassname.objects.all())```.
15. Just to give, for instance, to give some values the format is ```t = Topic(top_name= "Social Network")```
16. Then, ```t.save()```,to save and use the ```print(yourclassname.objects.all())```. This will give the changes made.
17. To use the admin interface with the models we register them in the admin.py file.
18. To register after import use the command: ```admin.site.register(class name)```.
19. After setup, the admin interface can be used to interact with the DB.
20. To fully use the DB and the Admin, we create a superuser using the command: ```python manage.py createsuperuser```. Provide a name, email, and password.

### Population Scripts

1. Useful to populate models with some "dummy" data.
2. Install Faker Library with ```pip install Faker```
3. Faker website: faker.readthedocs.io
4. To populate with the fake data created. Command: ```python fakescriptname.py```
5. The file script with the explanation is in the file Django/first_project/populate_first_app.py


### Django Forms

1. Usage:
   1. Quickly generate HTML form widgets.
   2. Validate data and process it into a Python data structure.
   3. Create form versions of our models and quickly update models from Forms.
2. First we create a forms.py file inside the Django application.
3. We then call Django's built-in forms classes.
4. Important topics:
   1. HTTP -> Hyper Text Transfer Protocol. They are designed to enable communication between a client and a server. The client submits a request and the server responds.
   2. Commonly used methods for this are GET and POST.
   3. GET -> Gets request data from a resource.
   4. POST -> Submits data to be processed to a resource.
5. CSRF Tag -> This is a Cross-Site Request Forgery token that secures the HTTP POST action initiated on the subsequent submission of the form.
6. CSRF is mandatory for Django to work. It works by using a "hidden input" which is a random code and checking that it matches the user's local site page.
7. ```{{ form.as_p }}``` means that the form tag is taken in the form of a paragraph tag for each. So there are appropriate break tags when necessary.
8. ```form.cleaned_data``` returns a dictionary of validated form input fields and their values, where string primary keys are returned as objects.
9. ```form.data``` returns a dictionary of un-validated form input fields and their values in string format (i.e. not objects).

### Relative URLs with Templates and Template Filters

1. Format: ```{% url 'basic_app:other' %}```
2. This will take you to the homepage: ```{% url 'index' %}```
3. This will take you to the database login page: ```{% url 'admin:index' %}```
4. https://docs.djangoproject.com/en/1.11/ref/templates/builtins -> Documentation for filters


### Django user authentication

1. The apps to be used are: ```django.contrib.auth``` and ```django.contrib.contenttypes```. These should be present in INSTALLED_APPS array.
2. For passwords we will use: the PBKDF2 algorithm with an SHA256 hash that is built-in in DJANGO.
3. Install for bcrypt and argon2: ```pip install bcrypt``` and ```pip install django[argon2]```.
4. Add this accordingly:
   ```
   PASSWORD_HASHERS = [
    
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher', ]
   ```

### USER Models

1. The user object has key features: Username, Email, Password, FirstName and Surname.
2. Other attributes for user object: is_active, is_staff, is_superuser.
3. To work with images in Python, we need to install pillow: ```pip install pillow```
4. If jpeg error is coming: ``` pip install pillow --global-option="build_ext" --global-option="--disable-jpeg" ```
5. User-uploaded content will go to the media folder, with the MEDIA_ROOT.
