from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import tweet
from django.contrib.auth.decorators import login_required
from .forms import TweetForm
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TweetListView(LoginRequiredMixin, ListView):
    model = tweet
    template_name = 'feed/home.html'
    ordering = ['-datetime']


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = tweet
    template_name = 'feed/create.html'
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)



@login_required
def home(request):
    context = {'tweets': tweet.objects.all}
    return render(request, 'feed/home.html', context)
