from .base import *
import pymysql
import os


DEBUG = False


ALLOWED_HOSTS += [
    '.compute.amazonaws.com',
]


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
