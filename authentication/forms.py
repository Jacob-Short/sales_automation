from authentication.models import MyUser
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)