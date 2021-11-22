from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    username= models.CharField(max_length=30, unique=True)
    password= models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    avatar_image = models.ImageField(upload_to='images/', null=True, blank=True) 

# Create your models here.
  
def __str__(self):
        return self.username


