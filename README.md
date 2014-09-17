# Django User Email Model

The basic necessities for using a custom user model that provides e-mail based
authentication instead of a username.

## Install

`pip install django-email-user-model`

## Config

Add `django_email_user_model` to your `INSTALLED_APPS` list.

Example:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_email_user_model',
)
```

In you Django settings.py set the `AUTH_USER_MODEL` to 
the `EmailUserModel` from the `django_email_user_model` app.

```python
AUTH_USER_MODEL = 'django_email_user_model.EmailUserModel'
```

Enable the authentication backend from `django_email_user_model`

```python
AUTHENTICATION_BACKENDS = (
    ('django_email_user_model.backends.EmailAuthBackend'),
)
```
