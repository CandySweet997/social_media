from django.shortcuts import render
# from .forms import SignupForm ,LoginForm
from . import forms


def signup(request):
    form = forms.SignupForm()
    if request == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["password"])

    return render(request, 'register2App/signup.html', {"form": form})


def login(request):
    form = forms.LoginForm()
    if request == 'POST':
        form = forms.LoginForm(request.POST)

    return render(request, 'register2App/login.html', {"form": form})


def home(request):
    return render(request, 'register2App/home.html')
