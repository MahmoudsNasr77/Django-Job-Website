from distutils.command.upload import upload
from math import trunc
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import localtime

from django.utils.text import Truncator
from accounts.models import Profile
class category(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class blog(models.Model):
    title=models.CharField(max_length=150)
    category=models.ForeignKey(category,related_name='post_category',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='post_owner',on_delete=models.CASCADE)
    description=models.TextField(max_length=1000)
    publish_at=models.DateTimeField(auto_created=True,auto_now_add=True)
    slug = models.SlugField(null=False,blank=True,primary_key=True)  
    image=models.ImageField(upload_to='post_image')
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(blog,self).save(*args,**kwargs)

    
class comment(models.Model):
    comment=models.TextField(max_length=2500,null=True,blank=True) 
    user=models.ForeignKey(User,related_name='comment_owner',on_delete=models.CASCADE)  
    blog=models.ForeignKey(blog,related_name='comment',on_delete=models.CASCADE)
    publish_at=models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return self.comment
