from django.urls import path
from .bulk_db import gen_data


urlpatterns = [
    path('/restaurants/database', gen_data, name='restaurant_database'),
]