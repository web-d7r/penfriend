from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('gender', 'birth_date', 'about_me', 'country', 'city')
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'})
        }
