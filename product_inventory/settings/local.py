from .base import *
from decouple import config
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config("DB_NAME"),
       'USER': config("DB_USER"),
       'PASSWORD': config("DB_PASS"),
       'HOST': config("DB_HOST"),
       'PORT': config("DB_PORT"),
   }
}
