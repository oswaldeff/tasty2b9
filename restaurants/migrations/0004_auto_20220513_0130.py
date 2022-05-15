# Generated by Django 3.2 on 2022-05-13 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20220512_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='이름')),
            ],
            options={
                'verbose_name_plural': '2. 서브 카테고리',
                'db_table': 'subcategories',
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='MainCategory',
        ),
        migrations.AlterModelOptions(
            name='maincategory',
            options={'verbose_name_plural': '1. 메인 카테고리'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name_plural': '4. 메뉴'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name_plural': '3. 음식점'},
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='category',
            new_name='main_category',
        ),
        migrations.AlterModelTable(
            name='maincategory',
            table='maincategories',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurants.subcategory'),
        ),
    ]