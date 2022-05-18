from django.http import HttpResponse, HttpRequest
from .scraper import get_restaurant_main_info
from .naver_api import get_restaurant_sub_info, get_restaurant_lat_lng
from restaurants.models import MainCategory, Restaurant
import math
import random
import requests
import json
import time


# generate restaurant data
def gen_restaurant_data(request: HttpRequest):
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


# update restaurant star, img data
def update_restaurant_data(request: HttpRequest):
    header = {
        'authority': 'map.naver.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': 'NNB=ZHREYBKYJGZWA; ASID=7c6f74d40000017a324f783a0000004f; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; _ga=GA1.1.843260892.1631082249; _ga_8P4PY65YZ2=GS1.1.1631546146.1.0.1631546150.0; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; MM_NEW=1; NFS=2; NaverSuggestUse=use%26unuse; _gcl_au=1.1.684846510.1636646068; nx_ssl=2; page_uid=4bf320b5-0774-4667-9eca-95099ebb77e8',
        'expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
        'pragma': 'no-cache',
        'referer': 'https://map.naver.com/',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    
    for restaurant in Restaurant.objects.all():
        dummy_data = round(random.uniform(3.0, 4.7), 1)
        restaurant.naver_rating = dummy_data
        restaurant.save()
        
        url = f'https://map.naver.com/v5/api/search?caller=pcweb&query=강남%20{restaurant.name}'
        try:
            response = requests.get(url, headers=header)
            content_json = json.loads(response.content)['result']['place']['list'][0]
            thum_url = content_json['thumUrl']
            restaurant.img = thum_url
            restaurant.save()
        except:
            pass
    return HttpResponse(status=200)
