from pyexpat import model
from django.db import models

class info(models.Model):
    locations=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    def __str__(self):
         return self.email
