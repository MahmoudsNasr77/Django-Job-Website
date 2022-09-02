from dataclasses import field
from pyexpat import model
from django import forms
from .models import comment,blog

class CommentForm(forms.ModelForm):
    class Meta:    
        model=comment
        fields=('comment',)
class BlogForm(forms.ModelForm):
        class Meta:    
            model=blog
            fields="__all__"
            exclude=('slug','user')
