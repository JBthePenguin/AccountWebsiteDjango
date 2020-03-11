## ***!!! Coming soon !!!*** Base for a Django website with account

A starting point for a website with account registration and authentification. It's using [Django](https://www.djangoproject.com/foundation/), [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/), [Font Awesome](https://fontawesome.com/icons) and [Google Fonts](https://fonts.google.com/). It contains:
- template base that include navbar and footer templates
- templates for each page that extend base with header and main
- default admin site
- debug toolbar for development
- tests for views, templates and responsive design
- User custom model, a staff group.

### How to install?

#### First way: with his install bash script
Execute [install.sh]() with the command **source**. You can pass a new name for your root folder in parameter:
```shell
source install.sh YourWebsite
```
First you are asked to choose the place for the root directory of your website, and after you have to register the superuser at the end of the installation.

#### Second way: step by step
Clone me, create a virtual environment inside *AccountWebsiteDjango* with [virtualenv](https://virtualenv.pypa.io/en/stable/) (*!!! maybe you have to install !!!*) and activate it:
```shell
$ git clone https://github.com/JBthePenguin/AccountWebsiteDjango.git
$ cd AccountWebsiteDjango
$ virtualenv -p python3 env
$ source env/bin/activate
```
Install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [django-bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/index.html), [django-fontawesome-5](https://github.com/BenjjinF/django-fontawesome-5), [selenium](https://selenium-python.readthedocs.io/)):
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
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the home page and visit the site.
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) to use the admin site.


### Tests
The tests use [selenium](https://selenium-python.readthedocs.io/) and maybe you have to install [GreckoWebdriver](https://github.com/mozilla/geckodriver/releases) to use firefox.
Run the tests:
```shell 
(env)$ python manage.py test -v 2
```
If you want to use Chrome, install [ChromeWebDriver](http://chromedriver.chromium.org/downloads) and change in *visitapp/tests/browser.py line 2*:
```python
from selenium.webdriver.chrome.webdriver import WebDriver
```
