from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import path

from contactscore.forms import ContactForm, ContactBookForm
from contactscore.models import Contact


# Create your views here.

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

@login_required(login_url='login_name')
def index_view(request):
    contacts = Contact.objects.all()
    return render(request, "contactscore/index.html", {"user": request.user, "contacts": contacts})


@login_required(login_url='login_name')
def add_contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        return redirect('index_name')

    form = ContactForm()
    return render(request, "contactscore/form.html", {"user": request.user, "form": form})


@login_required()
def add_contactbook_view(request):
    if request.method == "POST":
        form = ContactBookForm(request.POST)
        contact_book = form.save(commit=False)
        contact_book.user = request.user
        contact_book.save()
        return redirect('index_name')

    form = ContactBookForm()
    return render(request, "contactscore/form.html", {"user": request.user, "form": form})


urlpatterns = [
    path("login", login_view, name='login_name'),
    path("", index_view, name='index_name'),
    path("add-contact", add_contact_view, name='add_contact_name'),
    path("add-contactbook", add_contactbook_view, name='add_contactbook_name'),
]
