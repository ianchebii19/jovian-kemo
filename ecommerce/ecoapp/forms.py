from tkinter import Widget
from django.contrib.auth.models import User
from django import forms
from . models import Customer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password','class': 'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model=User
        fields=[ 'username', 'email', 'password1', 'password2' ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'city', 'location', 'county', 'mobile']  # Corrected 'fields' spelling
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'})
        }


  



    