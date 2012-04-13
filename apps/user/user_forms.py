#coding=utf-8
from django import forms

class RegisterForm(forms.Form):
    username = forms.RegexField(request=True, min_length=5, max_length=20, widget=forms.TextInput)
    password = forms.RegexField(request=True, min_length=5, max_length=20, widget=forms.PasswordInput)
    

