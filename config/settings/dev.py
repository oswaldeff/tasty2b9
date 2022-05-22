from .base import *
import os


ALLOWED_HOSTS += [
    '127.0.0.1', 
    'localhost',
    os.environ.get('LOCAL_HOST'),
]


INTERNAL_IPS = [
    '127.0.0.1',
    os.environ.get('LOCAL_HOST'),
]

import pymysql
# pymysql setting
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
                'charset': 'utf8mb4',
            },
            'HOST': os.environ.get('DATABASES_HOST'),
            'NAME': os.environ.get('DATABASES_NAME'),
            'USER': os.environ.get('DATABASES_USER'),
            'PASSWORD': os.environ.get('DATABASES_PASSWORD'),
            'PORT': os.environ.get('DATABASES_PORT'),
        }
}