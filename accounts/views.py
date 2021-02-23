from django.shortcuts import render, redirect
from .forms import signupForm
from django.contrib import messages


def register(request):
    if request == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'account created')
            return redirect('/login')
    else:
        form = signupForm()

    return render(request, 'accounts/signup.html', {'form': form})
