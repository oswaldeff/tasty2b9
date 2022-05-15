# Generated by Django 3.2 on 2022-05-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20220513_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.DecimalField(decimal_places=7, default=None, max_digits=10, null=True, verbose_name='위도'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.DecimalField(decimal_places=7, default=None, max_digits=10, null=True, verbose_name='경도'),
        ),
    ]