Django is a free and open source web framework.

It is important to use venv(virtual environment) as it allows you to have a virtual environment of python and packages on computer.

Virtual environment contains the newer version of the package. In anaconda the virtual environment handler is included.

To create virtual environemtn with conda:
~~~ conda create --name myEnv django ~~~

activate environment: ~~~ activate myEnv ~~~

Anything installed with pip or conda will be only within that environment. So it is easier to craete multiple virtual environments with different versions and packages.

Deactivate the environment: ~~~ deactivate environment ~~~

