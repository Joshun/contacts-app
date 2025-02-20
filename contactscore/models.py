from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ContactBook(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)

    @property
    def view_url(self):
        return reverse('view_contactbook_name', kwargs={"contact_book_id": self.pk})

    @property
    def edit_url(self):
        return reverse('edit_contactbook_name', kwargs={"contact_book_id": self.pk})

    @property
    def add_contact_url(self):
        return reverse('add_contact_name', kwargs={"contact_book_id": self.pk})



class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    photo = models.FileField()
    contact_book = models.ForeignKey('ContactBook', on_delete=models.CASCADE)

    # user = models.User...
    # labels = models.ManyToManyField





