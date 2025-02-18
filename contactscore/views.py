from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import path


# Create your views here.

@login_required(login_url='login_name')
def index_view(request):
    return render(request, "contactscore/index.html", {"user": request.user})


def login_view(request):
    if request.method == "GET":
        return render(request, "contactscore/login.html", {"errors": None})
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index_name')
    else:
        return render(request, "contactscore/login.html", {"errors": "login_failed"})


urlpatterns = [
    path("login", login_view, name='login_name'),
    path("", index_view, name='index_name'),
]
