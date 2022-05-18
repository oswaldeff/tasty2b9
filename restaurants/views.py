from django.shortcuts import render
from django.db.models import Q, OuterRef, Subquery
from django.http import HttpRequest
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from .models import Restaurant, Menu
import os
import re


# Create your views here.


def get_context():
    context = {
        'NAVER_MAP_CLIENT_ID': os.environ.get('NAVER_MAP_CLIENT_ID'),
        'LOCAL_HOST': os.environ.get('LOCAL_HOST'),
        'SECTION': 'home',
        'PAGE': 1
    }
    return context


def home(request: HttpRequest):
    template_name = 'restaurants/home.html'
    context = get_context()
    context.update({
        'SORT': 'distance'
    })
    
    if request.GET.get('sort', ''):
        sort = request.GET.get('sort', '')
        sort_set = {
            '거리': 'distance',
            '별점': '-naver_rating',
            '좋아요': None,
            '가격': 'min_price'
        }
        context.update({
            'SORT': sort_set[sort]
        })
    
    if request.GET.get('search', ''):
        search_keyword = request.GET.get('search', '')
        search_keyword = search_keyword.replace(' ', '')
        search_keyword = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', search_keyword)
        
        page = request.GET.get('page', '1')
        q = Q()
        q.add(Q(sub_category__icontains=search_keyword), q.OR)
        q.add(Q(name__icontains=search_keyword), q.OR)
        
        if context['SORT'] == 'min_price':
            sub_queryset = Menu \
                .objects \
                .filter(restaurant=OuterRef('id')) \
                .order_by('price')
            queryset = Restaurant \
                .objects \
                .filter(q) \
                .distinct() \
                .annotate(min_price=Subquery(sub_queryset.values('price')[:1])) \
                .order_by(context['SORT'])
        else:
            queryset = Restaurant \
                .objects \
                .filter(q) \
                .distinct() \
                .order_by(context['SORT'])
        paginator = Paginator(queryset, 5)
        restaurants = paginator.get_page(page)
        
        context.update({
            'PAGE': page,
            'SEARCH_KEYWORD': search_keyword,
            'RESTAURANTS': restaurants
        })
    
    if request.GET.get('category', ''):
        category = request.GET.get('category', '')
        
        page = request.GET.get('page', '1')
        q = Q()
        q.add(Q(main_category__name=category), q.AND)
        if context['SORT'] == 'min_price':
            sub_queryset = Menu \
                .objects \
                .filter(restaurant=OuterRef('id')) \
                .order_by('price')
            queryset = Restaurant \
                .objects \
                .select_related('main_category') \
                .filter(q) \
                .annotate(min_price=Subquery(sub_queryset.values('price')[:1])) \
                .order_by(context['SORT'])
        else:
            queryset = Restaurant \
                .objects \
                .select_related('main_category') \
                .filter(q) \
                .order_by(context['SORT'])
        paginator = Paginator(queryset, 5)
        restaurants = paginator.get_page(page)
        
        context.update({
            'PAGE': page,
            'CATEGORY': category,
            'RESTAURANTS': restaurants
        })
    
    return render(request, template_name, context)


def restaurant_detail(request: HttpRequest, restaurant_id):
    template_name = 'restaurants/detail.html'
    context = get_context()
    referer = request.META.get('HTTP_REFERER')
    restaurant = Restaurant.objects.get(id=restaurant_id)
    menu = Menu.objects.filter(restaurant=restaurant).order_by('id')
    context.update({
        'RESTAURANT': restaurant,
        'MENU': menu,
        'REFERER': referer
    })
    
    return render(request, template_name, context)