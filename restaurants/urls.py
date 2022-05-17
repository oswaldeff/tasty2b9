from django.urls import path
from .views import home


app_name = 'restaurants'


urlpatterns = [
    path('', home, name='home'),
]
