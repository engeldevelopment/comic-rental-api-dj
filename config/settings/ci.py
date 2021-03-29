from .base import *


INSTALLED_APPS += [
    'django_mutpy',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'apps/db.sqlite3'
    }
}