# Generated by Django 3.2 on 2022-05-12 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
            ],
            options={
                'verbose_name_plural': '1. 카테고리',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('near_station', models.CharField(max_length=100, verbose_name='인근 역')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('naver_rating', models.PositiveIntegerField(default=None, null=True, verbose_name='네이버 별점')),
                ('search_count', models.PositiveIntegerField(default=0, verbose_name='검색 카운트')),
                ('is_delete', models.BooleanField(default=False, verbose_name='삭제')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.category')),
            ],
            options={
                'verbose_name_plural': '2. 음식점',
                'db_table': 'restaurants',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='가격')),
                ('is_delete', models.BooleanField(default=False, verbose_name='삭제')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'verbose_name_plural': '3. 메뉴',
                'db_table': 'menu',
            },
        ),
    ]