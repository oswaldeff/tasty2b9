from django.shortcuts import render
from django.db.models import Q
from django.http import HttpRequest
from django.core.paginator import Paginator
from .models import MainCategory, Restaurant
import os


# Create your views here.


def home(request: HttpRequest):
    template_name = 'restaurants/home.html'
    context = {
        'NAVER_MAP_CLIENT_ID': os.environ.get('NAVER_MAP_CLIENT_ID'),
        'LOCAL_HOST': os.environ.get('LOCAL_HOST'),
        'SECTION': 'home'
    }
    q = Q()
    
    if request.GET.get('search', ''):
        search_keyword = request.GET.get('search', '')
        queryset = Restaurant.objects.all().order_by('distance')[:5]
        context['RESTAURANTS'] = queryset
    
    if request.GET.get('category', ''):
        category = request.GET.get('category', '')
        page = request.GET.get('page', '1')
        context['CATEGORY'] = category
        queryset = Restaurant.objects.select_related('main_category').filter(main_category__name=category).order_by('distance')
        paginator = Paginator(queryset, 3)
        queryset = paginator.get_page(page)
        context['CATEGORY'] = category
        context['PAGE'] = page
        context['RESTAURANTS'] = queryset
    
    return render(request, template_name, context)
