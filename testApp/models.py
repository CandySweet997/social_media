
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Tw (models.Model):

    text = models.CharField(max_length=281, default="")
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
