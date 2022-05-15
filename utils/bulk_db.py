from django.http import HttpResponse, HttpRequest
from .scraper import get_restaurant_main_info
from .naver_api import get_restaurant_sub_info, get_restaurant_lat_lng
from restaurants.models import MainCategory, Restaurant
import math


def gen_data(request: HttpRequest):
    MainCategory.objects.bulk_create([
        MainCategory(name='한식'),
        MainCategory(name='일식'),
        MainCategory(name='중식'),
        MainCategory(name='양식')
    ])
    korean_style_food = MainCategory.objects.get(name='한식')
    japanese_style_food = MainCategory.objects.get(name='일식')
    chinese_style_food = MainCategory.objects.get(name='중식')
    western_style_food = MainCategory.objects.get(name='양식')
    
    restaurant_databases = []
    main_info_content = get_restaurant_main_info()
    for main_info in main_info_content:
        main_category_database = None
        restaurant_database = {
            'main_category': None,
            'sub_category': None,
            'near_station': None,
            'name': None,
            'address': None,
            'latitude': None,
            'longitude': None,
            'distance': None
        }
        sub_info_content = get_restaurant_sub_info(main_info['near_station'], main_info['name'])
        if (not sub_info_content['address']) or ('서울특별시 강남구' not in sub_info_content['address']):
            continue
        
        lat_lng_content = get_restaurant_lat_lng(sub_info_content['address'])
        latitude = float(lat_lng_content['latitude'])
        longitude = float(lat_lng_content['longitude'])
        pi = 3.141592653589
        radian_latitude_maclaurin = 37.511875 * pi / 180
        radian_longitude_maclaurin = 127.050206 * pi /180
        radian_latitude_restaurant = latitude * pi / 180
        radian_longitude_restaurant = longitude * pi / 180
        distance = round(6378.137 * math.acos(math.cos(radian_latitude_maclaurin)*math.cos(radian_latitude_restaurant)*math.cos(radian_longitude_restaurant-radian_longitude_maclaurin) + math.sin(radian_latitude_maclaurin)*math.sin(radian_latitude_restaurant)), 2)
        
        if main_info['main_category'] == '한식':
            main_info['main_category'] = korean_style_food
        elif main_info['main_category'] == '일식':
            main_info['main_category'] = japanese_style_food
        elif main_info['main_category'] == '중식':
            main_info['main_category'] = chinese_style_food
        elif main_info['main_category'] == '양식':
            main_info['main_category'] = western_style_food
        
        restaurant_database['main_category'] = main_info['main_category']
        restaurant_database['sub_category'] = sub_info_content['sub_category']
        restaurant_database['near_station'] = main_info['near_station']
        restaurant_database['name'] = main_info['name']
        restaurant_database['address'] = sub_info_content['address']
        restaurant_database['latitude'] = latitude
        restaurant_database['longitude'] = longitude
        restaurant_database['distance'] = distance
        restaurant_databases.append(restaurant_database)
    
    Restaurant.objects.bulk_create([Restaurant(**data) for data in restaurant_databases], ignore_conflicts=True)
    return HttpResponse(status=200)
