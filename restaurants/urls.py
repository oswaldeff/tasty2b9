from django.urls import path
from .views import home, restaurant_detail


app_name = 'restaurants'


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:restaurant_id>', restaurant_detail, name='detail')
]
