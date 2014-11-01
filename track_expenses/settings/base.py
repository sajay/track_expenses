"""
This file settings/base.py has the settings that are common to all instances of
the project.

Django settings for track_expenses project.


For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ""


# False by default in base.py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

#REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES':[
#         'rest.framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ] 
#}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 #   'rest_framework',
    'admintool',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'track_expenses.urls'

WSGI_APPLICATION = 'track_expenses.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': '',
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':'',
#        'NAME':'expenses_db',
#        'USER':'root',
#        'PASSWORD':'',
#        'HOST':'127.0.0.1',
#        'PORT':'3306',
    },
#    'development': {
#        'ENGINE':'django.db.backends.mysql',
#        'NAME':'expenses_db',
#        'USER':'sanix',
#        'PASSWORD':'pyp@ss',
#        'HOST':'127.0.0.1',
#        'PORT':'3306',
#    },
}
################################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'track_expenses.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'INFO',
        },
        'admintool.views': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    }
}


################################################
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True


# Commented since we are getting a runtime warning:
# received a naive datetime while time zone support is active.
#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)
