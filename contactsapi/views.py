from django.shortcuts import render
from django.urls import path
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

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


urlpatterns = [
    path("contact-book", ContactbookListView.as_view()),
    path("contact", ContactListView.as_view()),
]
