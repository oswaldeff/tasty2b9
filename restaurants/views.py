from django.shortcuts import render
from django.db.models import Q
from django.http import HttpRequest
from django.core.paginator import Paginator
from .models import MainCategory, Restaurant
import os
import re


# Create your views here.


def home(request: HttpRequest):
    template_name = 'restaurants/home.html'
    context = {
        'NAVER_MAP_CLIENT_ID': os.environ.get('NAVER_MAP_CLIENT_ID'),
        'LOCAL_HOST': os.environ.get('LOCAL_HOST'),
        'SECTION': 'home',
        'AUTH': False,
        'CATEGORY': False,
        'SEARCH_KEYWORD': False,
        'ORDER_BY': False
    }
    q = Q()
    
    if request.GET.get('search', ''):
        search_keyword = request.GET.get('search', '')
        search_keyword = search_keyword.replace(' ', '')
        search_keyword = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', search_keyword)
        
        page = request.GET.get('page', '1')
        q.add(Q(sub_category__icontains=search_keyword), q.OR)
        q.add(Q(name__icontains=search_keyword), q.OR)
        queryset = Restaurant \
            .objects \
            .filter(q) \
            .order_by('distance')
        
        paginator = Paginator(queryset, 5)
        restaurants = paginator.get_page(page)
        
        context.update({
            'SEARCH_KEYWORD': search_keyword,
            'PAGE': page,
            'RESTAURANTS': restaurants
        })
    
    if request.GET.get('category', ''):
        category = request.GET.get('category', '')
        
        page = request.GET.get('page', '1')
        queryset = Restaurant \
            .objects \
            .select_related('main_category') \
            .filter(main_category__name=category) \
            .order_by('distance')
        paginator = Paginator(queryset, 5)
        restaurants = paginator.get_page(page)
        
        context.update({
            'CATEGORY': category,
            'PAGE': page,
            'RESTAURANTS': restaurants
        })
    
    return render(request, template_name, context)
