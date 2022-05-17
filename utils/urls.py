from django.urls import path
from .bulk_db import gen_data, update_data


urlpatterns = [
    path('/restaurants/database', gen_data, name='restaurant_database'),
    path('/restaurants/star', update_data, name='restaurant_star'),
]