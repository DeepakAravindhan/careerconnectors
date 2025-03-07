from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Job, StudyMaterial






# ✅ Login Form (Add this if missing)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

