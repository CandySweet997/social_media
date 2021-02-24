from django import forms
from .models import Tw


class TestForm(forms.ModelForm):

    class Meta:
        model = Tw
        fields = "__all__"