from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from contactscore.models import ContactBook, Contact


# TODO: add auth to these views

class ContactBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBook
        fields = '__all__'

class ContactbookListView(ListAPIView):
    queryset = ContactBook.objects.all()
    serializer_class = ContactBookSerializer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



@api_view(['GET'])
@login_required
def contact_totals_view(request):
    contact_books = ContactBook.objects.for_user(request.user)
    contacts = Contact.objects.filter(contact_book__in=contact_books)
    return Response({
        "contacts": contacts.count(),
        "contact_books": contact_books.count(),
    })


urlpatterns = [
    path("contact-book", ContactbookListView.as_view()),
    path("contact", ContactListView.as_view()),
    path("totals", contact_totals_view),
]
