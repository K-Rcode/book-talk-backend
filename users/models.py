from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    #  Require email field for authentication
    
