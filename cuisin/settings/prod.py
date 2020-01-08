from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         # Backends disponibles : 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'cuis-in',
         'USER': 'cuis-in', # TODO 
         'PASSWORD': 'OUFf7yKZ8AKSuuTq',
         'HOST': '127.0.0.1',
         'PORT': '',
         'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
         },
     }
}