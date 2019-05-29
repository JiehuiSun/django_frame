# coding:utf-8

from .base import *
import logging.config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'sqllite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmmm',
        'USER': 'xxx',
        'PASSWORD': '***',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

"""
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        '',
    ],
    'EXCEPTION_HANDLER': '',
}
"""

log_conf = os.path.join(BASE_DIR, "conf/dev_log.conf")
logging.config.fileConfig(log_conf)

