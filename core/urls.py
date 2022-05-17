from django.urls import path
from .views import proxy_home


app_name = 'core'


urlpatterns = [
    path('', proxy_home, name='proxy-home'),
]
