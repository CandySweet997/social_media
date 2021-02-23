from django import forms
from django.core import validators
import string

class Testform(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    phonenumber = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)
    def clean_firstname (self):
        inputifirstname = self.cleaned_data["firstname"]
        # inputPassword = user_cleaned_data['password']
        # inputConfirmpassword = user_cleaned_data['confirmpassword']
        # inputPhone = user_cleaned_data['phonenumber']

        if len(inputifirstname) < 8:
            raise forms.ValidationError('Password length must be more than 8 characters')
        return inputifirstname