from django import forms
from .models import Email, URL
from django.contrib.auth.models import User

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['sender', 'receiver', 'subject', 'content']

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['link', 'domain']

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']