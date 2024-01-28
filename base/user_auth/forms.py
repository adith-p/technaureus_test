from django import forms
from django.forms import widgets


class loginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=widgets.PasswordInput)