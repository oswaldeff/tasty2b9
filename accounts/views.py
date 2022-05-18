from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .models import User
from .forms import SignupForm


# Create your views here.


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('restaurants:home')
    template_name = 'accounts/signup.html'
    
    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.get_form()
        email = request.POST['email']
        password = request.POST['password1']
        super().post(request, *args, **kwargs)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(reverse('restaurants:home'))


def logout_view(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('restaurants:home'))