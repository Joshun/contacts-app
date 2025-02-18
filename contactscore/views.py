from django.shortcuts import render
from django.urls import path


# Create your views here.

def index(request):
    return render(request, "contactscore/index.html")


urlpatterns = [
    path("", index),
]
