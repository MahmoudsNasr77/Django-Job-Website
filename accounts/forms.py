from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
        
