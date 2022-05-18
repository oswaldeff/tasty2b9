from django.urls import path
from .bulk_db import gen_restaurant_data, update_restaurant_data, gen_menu_data


urlpatterns = [
    path('/restaurants/database', gen_restaurant_data, name='restaurant_database'),
    path('/restaurants/star/img', update_restaurant_data, name='restaurant_star_img'),
    path('/meals/database', gen_menu_data, name='meal_database'),
]