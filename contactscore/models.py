from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    photo = models.FileField()

    contact_book = models.ForeignKey('ContactBook', on_delete=models.CASCADE)

    # user = models.User...
    # labels = models.ManyToManyField


class ContactBook(models.Model):
    name = models.CharField(max_length=255)
    # user = models.User ...
    description = models.CharField(max_length=255, null=True, blank=True)


