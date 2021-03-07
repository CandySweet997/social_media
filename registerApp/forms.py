from django import forms
from django.core import validators
from . models import user
import string
from .models import profile



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image', 'bio']



