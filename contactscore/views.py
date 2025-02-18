from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path


# Create your views here.

@login_required(login_url='login_name')
def index(request):
    return render(request, "contactscore/index.html")

def login(request):
    if request.method == "GET":
        return render(request, "contactscore/login.html", {"errors": None})
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
    else:
        return render(request, "contactscore/login.html", {"errors": "login_failed"})

urlpatterns = [
    path("login", login, name='login_name'),
    path("", index),
]
