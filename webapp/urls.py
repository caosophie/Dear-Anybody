from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("submit/", views.submit, name="submit"),
    path("stories/", views.stories, name="stories")
]