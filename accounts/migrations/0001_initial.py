# Generated by Django 3.2 on 2022-05-17 21:01

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='업데이트날짜')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('password', models.CharField(blank=True, max_length=255, null=True, verbose_name='비밀번호')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('is_staff', models.BooleanField(default=False, verbose_name='스태프')),
                ('is_admin', models.BooleanField(default=False, verbose_name='어드민')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='슈퍼유저')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': '1. 유저',
                'db_table': 'users',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
