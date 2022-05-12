from django.urls import path
from .scraper import get_restaurant_name
from .naver_api import get_restaurant_info, get_restaurant_lat_lng


urlpatterns = [
    path('/restaurants/names', get_restaurant_name, name='restaurant_name'),
    path('/restaurants/infomations', get_restaurant_info, name='restaurant_info'),
    path('/restaurants/latlng', get_restaurant_lat_lng, name='restaurant_lat_lng'),
]