from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class myuser(AbstractUser):
     email=models.EmailField(max_length=254,blank=False,unique=True)
     first_name=models.CharField(blank=False,max_length=150)
     def __str__(self):
          return self.first_name

