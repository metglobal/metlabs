"""
Django settings for production environment.
This file should be linked as settings_local.py in settings directory.
"""

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'labs.example.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'labs',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = 'http://labs.example.com/static/'
