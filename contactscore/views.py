from typing import Optional

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path, reverse

from contactscore.forms import ContactForm, ContactBookForm
from contactscore.models import Contact, ContactBook


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


def logout_view(request):
    logout(request)
    return redirect('index_name')


@login_required(login_url='login_name')
def index_view(request):
    contact_books = ContactBook.objects.for_user(request.user)
    return render(request, "contactscore/index.html", {"user": request.user, "contact_books": contact_books})


@login_required(login_url='login_name')
def add_contact_view(request, contact_book_id: int):
    contact_book = get_object_or_404(ContactBook, pk=contact_book_id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        contact = form.save(commit=False)
        contact.contact_book = contact_book
        contact.save()
        return redirect(contact_book.view_url)

    form = ContactForm()
    return render(request, "contactscore/form.html", {"user": request.user, "form": form, "form_title": "Add new contact", "from": contact_book.view_url })


@login_required()
def edit_contact_view(request, contact_id: int):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        form.save()
        return redirect(contact.contact_book.view_url)

    form = ContactForm(instance=contact)
    return render(request, "contactscore/form.html", {"user": request.user, "form": form, "form_title": "Edit contact", "from": contact.contact_book.view_url })


@login_required()
def add_edit_contactbook_view(request, contact_book_id: Optional[int] = None):
    form_args = {}
    if contact_book_id is not None:
        contact_book = get_object_or_404(ContactBook, pk=contact_book_id)
        form_args["instance"] = contact_book

    if request.method == "POST":
        form_args["data"] = request.POST
        form = ContactBookForm(**form_args)
        contact_book = form.save(commit=False)
        contact_book.user = request.user
        contact_book.save()
        return redirect('index_name')

    form = ContactBookForm(**form_args)
    return render(request, "contactscore/form.html", {"user": request.user, "form": form, "form_title": "Add new contact book", "from": reverse('index_name')})


@login_required()
def view_contactbook_view(request, contact_book_id: int):
    contact_book = get_object_or_404(ContactBook, pk=contact_book_id)
    contacts = contact_book.contact_set.all()
    return render(request, "contactscore/contactbook.html", {"user": request.user, "contact_book": contact_book, "contacts": contacts})


urlpatterns = [
    path("login", login_view, name='login_name'),
    path("logout", logout_view, name='logout_name'),
    path("", index_view, name='index_name'),
    path("add-contact/<int:contact_book_id>", add_contact_view, name='add_contact_name'),
    path('edit-contact/<int:contact_id>', edit_contact_view, name='edit_contact_name'),

    path("add-contactbook", add_edit_contactbook_view, name='add_contactbook_name'),
    path("edit-contactbook/<int:contact_book_id>",add_edit_contactbook_view,  name='edit_contactbook_name'),
    path("view-contactbook/<int:contact_book_id>", view_contactbook_view, name='view_contactbook_name')
]
