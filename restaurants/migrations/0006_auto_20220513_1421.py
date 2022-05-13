# Generated by Django 3.2 on 2022-05-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20220513_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='이름'),
        ),
    ]
