from django.shortcuts import render ,redirect
from .models import tweet
from django.contrib.auth.decorators import login_required
from .forms import tweetForm

@login_required
def home(request):
    context = {'tweets': tweet.objects.all}
    return render(request, 'feed/home.html', context)

def createTweet (request):
    form = tweetForm()
    if request.method == "POST":
        form = tweetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request, 'feed/home.html', {'tweetform': form})


