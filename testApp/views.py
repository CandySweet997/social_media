from django.shortcuts import render, redirect
from .forms import TestForm
from .models import Tw


def test(request):
    form = TestForm()
    if (request.method == "POST"):
        form = TestForm(request.POST)
        print("is not valid ")
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("/test")
    print("not saved")
    return render(request, "testApp/test.html", {"Formtest": form})
#
# def ctreatetest(request):
#     tweet = Tw.objects.all()
#     return render(request,"testApp/test.html", {"tweet": tweet})