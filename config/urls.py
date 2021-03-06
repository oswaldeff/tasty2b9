"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from restaurants.views import home

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # core
    path('', include('core.urls'), name='core'),
    # restaurants
    path('restaurants/', include('restaurants.urls'), name='restaurants'),
    # accounts
    path('accounts/', include('accounts.urls'), name='accounts'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        # debug toolbar
        path('__debug__/', include(debug_toolbar.urls)),
        # utils
        path('utils', include('utils.urls')),
    ]