from django import forms
from django.db import models

 # Create your models here.

class User(models.Model):
     name = models.CharField(max_length=100)
     dob = models.DateField()
     email = models.EmailField(max_length=50)
     phone = models.IntegerField()
