from .base import *


DEBUG = False


ALLOWED_HOSTS += [
    
]


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
