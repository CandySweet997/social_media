from django import forms
from django.core import validators
from . models import user
import string
from .models import profile



class profileForm(forms.Form):
    class Meta:
        model = profile
        fields = '__all__'


class LoginForm(forms.Form):
    ussername = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(50)])
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):

        name = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(50)])
        phone = forms.CharField(max_length=11)
        birthdate = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y"))
        password = forms.CharField(widget=forms.PasswordInput)
        confirmpassword = forms.CharField(widget=forms.PasswordInput)
        #Gender = [('male', 'Male'), ('female', 'Female')]
        #gender = forms.CharField(widget=forms.Select(choices=Gender))


        def clean(self):
            user_clean_data = super().clean()
            inputPassword = user_clean_data['password']
            if strong(inputPassword) == 'Weak':
                raise forms.ValidationError('Password is week ! ')
            if len(inputPassword) > 15:
                raise forms.ValidationError('Password length must be less than 15 characters')
            if len(inputPassword) < 8:
                raise forms.ValidationError('Password length must be more than 8 characters')
            inputConfirmpassword = user_clean_data['confirmpassword']
            inputPassword = user_clean_data['password']
            if inputPassword != inputConfirmpassword:
                raise forms.ValidationError('Passwords do not match ! ')
            #inputPhone = user_clean_data['phone']
            #if inputPhone[:2] != '09':
            #     raise forms.ValidationError('phone format in wrong ! ')
            # if inputPhone.strip() < 11:
            #     raise forms.ValidationError('phone format in wrong ! ')
            # if phone_checker(inputPhone) == False:
            #     raise forms.ValidationError('phone format in wrong ! ')



def strong(s):  # This is a script that checks input and says whether it is weak or strong
    if len(list(set(s) & set(string.ascii_lowercase))) > 0 and len(
            list(set(s) & set(string.ascii_uppercase))) > 0 and len(list(set(s) & set(string.digits))) > 0 and len(
        list(set(s) & set(string.punctuation))) > 0:
        return "Strong"
    else:
        return "Weak"

def phone_checker(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if i in s:
            return False
        elif i.upper() in s:
            return False

    return True


