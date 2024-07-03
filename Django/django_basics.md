Django is a free and open-source web framework.

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

#### Unapplied Migrations:

Migrations allow us to move databases from one design to another. This is also reversible.


