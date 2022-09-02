from dataclasses import field
from pyexpat import model
from django import forms
from .models import Apply,Job

class Applyfrom(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','website','cv','coverletter']
class Addjob(forms.ModelForm):
    class Meta:    
        model=Job
        fields='__all__'
        exclude=('user','slug')