from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=False, null=False ,default='default_user_pic.jpg')

    class Meta:
        managed = True
        db_table = 'users'
