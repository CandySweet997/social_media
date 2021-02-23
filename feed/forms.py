from .models import tweet
from django import forms

class tweetForm(forms.ModelForm):
  text = forms.CharField

 class Meta:
        model = tweet
        fields = ["text"]

