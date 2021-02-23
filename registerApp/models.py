from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')
    bio = models.TextField(default='')

    def __str__(self):
        return f'{self.user.username}'

