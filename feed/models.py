from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from Registration.registerApp.models import profile


class tweet(models.Model):
    text = models.TextField(max_length=280, default="")
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    #avatar = models.OneToOneField( profile, on_delete=models.CASCADE )

