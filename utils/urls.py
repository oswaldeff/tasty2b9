from django.urls import path
from .scraper import get_restaurant_name


urlpatterns = [
    path('/restaurants/names', get_restaurant_name, name='restaurant_name'),
]