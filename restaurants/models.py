from django.db import models
from core.models import TimeStampedModel


# Create your models here.


class MainCategory(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name='이름')
    
    class Meta:
        verbose_name_plural = '1. 카테고리'
        db_table = 'maincategories'
    
    def __str__(self):
        return str(self.name)


class Restaurant(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    main_category = models.ForeignKey(MainCategory, null=True, on_delete=models.SET_NULL, related_name='category_restaurant', verbose_name='메인 카테고리')
    sub_category = models.CharField(max_length=100, null=True, verbose_name='서브 카테고리')
    near_station = models.CharField(max_length=100, verbose_name='인근 역')
    name = models.CharField(max_length=100, unique=True, verbose_name='이름')
    address = models.CharField(max_length=255, verbose_name='주소')
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, default=None, verbose_name='위도')
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, default=None, verbose_name='경도')
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=None, verbose_name='거리')
    naver_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, default=None, verbose_name='네이버 별점')
    search_count = models.PositiveIntegerField(default=0, verbose_name='검색 카운트')
    is_delete = models.BooleanField(default=False, verbose_name='삭제')
    
    class Meta:
        verbose_name_plural = '2. 음식점'
        db_table = 'restaurants'
    
    def __str__(self):
        return str(self.id)


class Menu(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_menu')
    name = models.CharField(max_length=100, verbose_name='이름')
    price = models.PositiveIntegerField(default=0, verbose_name='가격')
    is_delete = models.BooleanField(default=False, verbose_name='삭제')
    
    class Meta:
        verbose_name_plural = '3. 메뉴'
        db_table = 'menu'
    
    def __str__(self):
        return str(self.id)