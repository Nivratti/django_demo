Django Demo
A prototype for launching new Django projects quickly. Implemented Custom user model and rest api.

## Features
- Custom user model
- Token-based auth
- Signup/login/logout

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed.
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/Nivratti/django_demo.git
$ cd django
$ pip install -r requirements.txt
```

3.  Set up the initial migration for our custom user models in `users` and build the database.

```
(django) $ python manage.py makemigrations users
(django) $ python manage.py migrate
```

4.  Create a superuser:

```
(django) $ python manage.py createsuperuser
```

5.  Confirm everything is working:

```
(django) $ python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).



## Endpoints

Login with your superuser account. Then navigate to all users. Logout. Sign up for a new account and repeat the login, users, logout flow.

- login - http://127.0.0.1:8000/api/v1/rest-auth/login/
- user details - http://127.0.0.1:8000/api/v1/rest-auth/user/
- logout - http://127.0.0.1:8000/api/v1/rest-auth/logout/
- signup - http://127.0.0.1:8000/api/v1/rest-auth/registration/

