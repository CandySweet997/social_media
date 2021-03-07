from .models import tweet
from django import forms


class TweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text']


