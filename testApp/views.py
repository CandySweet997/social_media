from django.shortcuts import render
from . import forms

def test(request):

    return render(request,"testApp/index.html")
