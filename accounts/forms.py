from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email']