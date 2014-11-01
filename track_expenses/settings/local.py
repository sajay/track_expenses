"""Development settings and globals."""
from __future__ import absolute_import
import os
from os.path import join, normpath
from .base import *

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


SECRET_KEY = os.environ["EXPENSES_SECRET_KEY"]

########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
#       'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'ENGINE':'django.db.backends.mysql',
        'NAME':'expenses_db',
        'USER':'sanix',
        'PASSWORD':'pyp@ss',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
########## END DATABASE CONFIGURATION

########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
#INSTALLED_APPS += (
#'debug_toolbar',
#)

#MIDDLEWARE_CLASSES += (
#'debug_toolbar.middleware.DebugToolbarMiddleware',
#)
#DEBUG_TOOLBAR_PATCH_SETTINGS = False
# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION
