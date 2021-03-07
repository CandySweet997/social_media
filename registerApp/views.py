from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as lo
import string
from django.contrib.auth.decorators import login_required
from .models import profile
from .forms import ProfileUpdateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = profile
#     template_name = 'registerApp/profileupdate.html'
#     fields = ['image', 'bio']
#     success_url = '/profile'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.username
#         return super().form_valid(form)
#
#     def test_func(self):
#         profile = self.get_object()
#         if self.request.user == profile.user:
#             return True
#         return False


def ProfileUpdateView(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            return redirect('/profile')
    else:
        pform = ProfileUpdateForm()

    return render(request, 'registerApp/profileupdate.html', {'pform': pform})


@login_required
def Profile(request):
    return render(request, 'registerApp/profile.html')


def logout(request):
    return render(request, 'registerApp/logout.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password2 == password1:
            if len(password1) < 8:
                messages.info(request, "Password length must be more than 8 characters!")
                return redirect('/signup')
            elif strong(password1) == 'Weak':
                messages.info(request, "Password is week!")
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                print("username taken ! ")
                messages.info(request, "Username Taken!")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('Account created ')
                return redirect("/login")


        else:
            messages.info(request, "Password not match ! ")

        return redirect('/signup')
    else:
        return render(request, 'registerApp/signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            lo(request, user)
            return redirect('/home')
        else:
            messages.info(request, "invalid credetial")
            return redirect('/login')
    else:

        return render(request, 'registerApp/login.html')


def strong(s):  # This is a script that checks input and says whether it is weak or strong
    if len(list(set(s) & set(string.ascii_lowercase))) > 0 and len(
            list(set(s) & set(string.ascii_uppercase))) > 0 and len(list(set(s) & set(string.digits))) > 0 and len(
        list(set(s) & set(string.punctuation))) > 0:
        return "Strong"
    else:
        return "Weak"
