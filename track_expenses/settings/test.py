from __future__ import absolute_import
from .base import *


DATABASES = {
    "default": {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'expenses_db',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    },
}

PASSWORD_HASHERS = (
'django.contrib.auth.hashers.MD5PasswordHasher',
)
