from django.shortcuts import render
from .models import Submission

def index(request):
    return render(request, "webapp/index.html", {
        "submissions" : Submission.objects.all()
    })