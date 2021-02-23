from django import forms
from django.core import validators
import string


class LoginForm(forms.Form):
    username = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(50)])
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(50)])
    last_name = forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(50)])
    phonenumber = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)

    # birthdate = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y"))
    # Gender = [('male', 'Male'), ('female', 'Female')]
    # gender = forms.CharField(widget=forms.Select(choices=Gender))
    def clean(self):
        user_cleaned_data = super().clean()
        inputPassword = user_cleaned_data['password']
        inputConfirmpassword = user_cleaned_data['confirmpassword']
        inputPhone = user_cleaned_data['phonenumber']

        if strong(inputPassword) == 'Weak':
            raise forms.ValidationError('Password is week ! ')
        elif len(inputPassword) < 8:
            raise forms.ValidationError('Password length must be more than 8 characters')
        elif inputPassword != inputConfirmpassword:
            raise forms.ValidationError('Passwords is not match ! ')
        elif inputPhone[:2] != '09':
            raise forms.ValidationError('phone format in wrong ! ')
        elif inputPhone.strip() < 11:
            raise forms.ValidationError('phone format in wrong ! ')
        elif phone_checker(inputPhone) == False:
            raise forms.ValidationError('phone format in wrong ! ')


# This is a script that checks input and says whether it is weak or strong
def strong(s):
    if len(list(set(s) & set(string.ascii_lowercase))) > 0 and len(
            list(set(s) & set(string.ascii_uppercase))) > 0 and len(list(set(s) & set(string.digits))) > 0 and len(
        list(set(s) & set(string.punctuation))) > 0:
        return "Strong"
    else:
        return "Weak"


def phone_checker(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        if i in s:
            return False
        elif i.upper() in s:
            return False

    return True
