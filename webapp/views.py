from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Submission
from .forms import CreateForm
from django.urls import reverse

def index(request):
    return render(request, "webapp/index.html", {
        "submissions" : Submission.objects.all(),
        "form" : CreateForm()
    })

def submit(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            name = form.cleaned_data["name"]
            Submission.objects.create(name=name, message=message)

        return HttpResponseRedirect(reverse("stories"))
    
    else:
        return render(request, "webapp/submit.html", {
            "form" : CreateForm()
        })

def stories(request):
    return render(request, "webapp/stories.html", {
        "submissions" : Submission.objects.all()
    })
