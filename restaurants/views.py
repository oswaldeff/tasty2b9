from django.shortcuts import render
from django.http import HttpRequest
import os


# Create your views here.


def home(request: HttpRequest):
    template_name = 'restaurants/home.html'
    context = {
        'NAVER_MAP_CLIENT_ID': os.environ.get('NAVER_MAP_CLIENT_ID'),
        'LOCAL_HOST': os.environ.get('LOCAL_HOST'),
        'PAGE': 'home'
    }
    return render(request, template_name, context)
