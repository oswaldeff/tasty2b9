from django.http import HttpRequest
from .scraper import get_restaurant_name
from .naver_api import get_restaurant_info, get_restaurant_lat_lng


def gen_restaurant_data(request: HttpRequest):
    pass