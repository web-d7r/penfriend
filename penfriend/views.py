from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, ProfileForm
from .models import Profile
import datetime
import requests


# Create your views here.
class IndexView(ListView):
    model = User
    paginate_by = 5
    template_name = 'home.html'
    context_object_name = 'users'

    def get_queryset(self):
        today = datetime.date.today() + datetime.timedelta(days=1)
        last_week = datetime.date.today() - datetime.timedelta(days=7)
        return User.objects.filter(last_login__range=(last_week, today)).order_by('-last_login')


class UserCreateView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        view = super(UserCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return view

    def get_success_url(self, **kwargs):
        return reverse('profile', kwargs={'pk': self.object.pk}, )


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile.html'
    form_class = ProfileForm

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.profile

    def get_initial(self):
        initial = super(ProfileUpdateView, self).get_initial()
        if self.request.user.profile.country:  # if record exists in country field
            return initial
        else:
            x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1]
            else:
                ip = self.request.META.get('REMOTE_ADDR')

        response = requests.get(f'https://ip-api.com/json/{ip}?fields=country,region,city').json()
        if len(response) < 3:
            return initial
        else:
            initial['country'] = response['country']
            initial['region'] = response['region']
            initial['city'] = response['city']
            return initial

    def get_success_url(self):
        return reverse('index')


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm


class Logout(LogoutView):
    next_page = 'index'
