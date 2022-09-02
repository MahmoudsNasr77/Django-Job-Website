from django.contrib.auth.models import User
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from msilib.schema import PublishComponent
from operator import mod
from pydoc import describe
from tkinter import CASCADE
from django.utils.text import slugify
from django.db import models
JOB_Type=( 
    ('Full Time','Full Time'),
    ('Part Time','Part Time')    
)
def image_upload(instance,filename):
    imagename,extention=filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)

class Job(models.Model):
    user=models.ForeignKey(User,related_name='Job_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_Type)
    description=models.TextField(max_length=1000)
    publish_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    exprince=models.IntegerField(default=1)
    jobcategory=models.ForeignKey('Jobcategory',on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)      
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)
class Category(models.Model):
    name =models.CharField(max_length=25)
    def __str__(self):
        return self.name
class Jobcategory(models.Model):
    name =models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Apply(models.Model):
     name =models.CharField(max_length=25)
     email=models.EmailField(max_length=256)
     website=models.URLField(max_length=256)
     cv=models.FileField(upload_to="apply/")
     coverletter=models.TextField(max_length=500)
     job=models.ForeignKey("Job",related_name="Apply_Job",on_delete=models.CASCADE)  
     created_at=models.DateTimeField(auto_now=True)
     
     def __str__(self):
        return self.name