## Base for a simple Django website

A starting point for a simple website using django and his default admin site.  
There is also a navbar using bootstrap 4 to be responsive.

### How to install?
Download *SimpleWebsite* and inside it:
- create a virtual environment with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*) and activate it:
```shell
$ virtualenv -p python3 env
$ source env/bin/activate
```
- install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/)):
```shell
(env)$ pip install -r requirements.txt
```
- make the migrations:
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
- create a *superuser*:
```shell
(env)$ python manage.py createsuperuser
```

### How to use?
Start the server:
```shell
(env)$ python manage.py runserver
```
With your favorite browser, go to url:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the home page
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) to use the admin site.
