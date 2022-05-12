from django.db import models
from core.models import TimeStampedModel


# Create your models here.


class Category(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='이름')
    
    class Meta:
        verbose_name_plural = '1. 카테고리'
        db_table = 'categories'
    
    def __str__(self):
        return str(self.id)


class Restaurant(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    near_station = models.CharField(max_length=100, verbose_name='인근 역')
    name = models.CharField(max_length=255, verbose_name='이름')
    address = models.CharField(max_length=255, verbose_name='주소')
    latitude = models.PositiveIntegerField(null=True, default=None, verbose_name='위도')
    longitude = models.PositiveIntegerField(null=True, default=None, verbose_name='경도')
    naver_rating = models.PositiveIntegerField(null=True, default=None, verbose_name='네이버 별점')
    search_count = models.PositiveIntegerField(default=0, verbose_name='검색 카운트')
    is_delete = models.BooleanField(default=False, verbose_name='삭제')
    
    class Meta:
        verbose_name_plural = '2. 음식점'
        db_table = 'restaurants'
    
    def __str__(self):
        return str(self.id)


class Menu(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='이름')
    price = models.PositiveIntegerField(default=0, verbose_name='가격')
    is_delete = models.BooleanField(default=False, verbose_name='삭제')
    
    class Meta:
        verbose_name_plural = '3. 메뉴'
        db_table = 'menu'
    
    def __str__(self):
        return str(self.id)