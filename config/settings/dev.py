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
