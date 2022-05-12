from cgi import print_form
from django.http import HttpRequest, JsonResponse
import requests
import os


# restaurant infomation
def get_restaurant_info(request: HttpRequest, near_station: str, name: str):
    api_url = f'https://openapi.naver.com/v1/search/local.json?query={name}'
    headers = {
        'X-Naver-Client-Id': os.environ.get('X_NAVER_CLIENT_ID'),
        'X-Naver-Client-Secret': os.environ.get('X_NAVER_CLIENT_SECRET')
    }
    naver_search_response = requests.get(api_url, headers=headers).content.decode('utf-8')
    
    content = {'is_exist': False}
    if naver_search_response['total'] == 1:
        content['is_exist'] = True
        content['near_station'] = near_station
        content['name'] = name
        content['category'] = naver_search_response['category']
        content['address'] = naver_search_response['roadAddress']
    return JsonResponse(content, status=200)


# restaurant latitude, longitude
def get_restaurant_lat_lng(request: HttpRequest, address: str):
    api_url = f'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}'
    headers = {
        'X-NCP-APIGW-API-KEY-ID': os.environ.get('NAVER_MAP_CLIENT_ID'),
        'X-NCP-APIGW-API-KEY': os.environ.get('NAVER_MAP_CLIENT_SECRET')
    }
    naver_geocode_response = eval(requests.get(api_url, headers=headers).content.decode('utf-8'))
    
    content = {
        'latitude': naver_geocode_response['addresses'][0]['x'],
        'longitude': naver_geocode_response['addresses'][0]['y']
    }
    return JsonResponse(content, status=200)