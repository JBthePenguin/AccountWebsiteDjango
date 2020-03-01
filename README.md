## Base for a simple Django website

A starting point for a simple website using [django](https://www.djangoproject.com/foundation/) and [django-bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/index.html):
- template base with navbar and footer
- home page
- default admin site
- debug toolbar for development

### How to install?

#### First way: with his install bash script
Execute [install_simple.sh](https://github.com/JBthePenguin/BasesWebsiteDjango/blob/master/install_scripts/install_simple.sh) with the command **source**. You can pass a new name for your root folder in parameter:
```shell
source install_simple.sh YourWebsite
```
First you are asked to choose the place for the root directory of your website, and after you have to register the superuser at the end of the installation.

#### Second way: step by step
Clone me, create a virtual environment inside *SimpleWebsiteDjango* with [virtualenv](https://virtualenv.pypa.io/en/stable/) (*!!! maybe you have to install !!!*) and activate it:
```shell
$ git clone https://github.com/JBthePenguin/SimpleWebsiteDjango.git
$ cd SimpleWebsiteDjango
$ virtualenv -p python3 env
$ source env/bin/activate
```
Install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [django-bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/index.html), [django-fontawesome-5](https://github.com/BenjjinF/django-fontawesome-5)):
```shell
(env)$ pip install -r requirements.txt
```
Make the migrations:
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
Create a *superuser*:
```shell
(env)$ python manage.py createsuperuser
```

### How to use?
Start the server (the virtual environment have to be activated):
```shell
(env)$ python manage.py runserver
```
With your favorite browser, go to url:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the home page
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) to use the admin site.
