from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def proxy_home(request):
    return HttpResponseRedirect(reverse('restaurants:home'))