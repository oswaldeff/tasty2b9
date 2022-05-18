from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def proxy_home(request: HttpRequest):
    return HttpResponseRedirect(reverse('restaurants:home'))