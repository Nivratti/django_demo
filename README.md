Django Demo
A prototype for launching new Django projects quickly. Implemented Custom user model and rest api.

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed.
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/Nivratti/django_demo.git
$ cd djangox
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration for our custom user models in `users` and build the database.

```
(djangox) $ python manage.py makemigrations users
(djangox) $ python manage.py migrate
```

4.  Create a superuser:

```
(djangox) $ python manage.py createsuperuser
```

5.  Confirm everything is working:

```
(djangox) $ python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).

