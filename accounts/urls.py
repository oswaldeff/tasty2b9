from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignupView, logout_view


app_name = 'accounts'


urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('logout', logout_view, name='logout'),
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
