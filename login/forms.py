from django import forms
from django.contrib.auth.models import User

class FormLogin(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'id': 'username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'id': 'password'})
    )