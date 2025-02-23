from django.core.validators import EmailValidator
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


    class ContactBookQuerySet(models.QuerySet):
        def for_user(self, user: User):
            return self.filter(user=user)

    objects = ContactBookQuerySet.as_manager()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=50, null=True, blank=True)
    home_number = models.CharField(max_length=50, null=True, blank=True)
    work_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True, validators=[EmailValidator(message="Invalid email address.")])
    address = models.TextField(null=True, blank=True)
    photo = models.FileField(upload_to='photo_uploads', blank=True, null=True)
    contact_book = models.ForeignKey('ContactBook', on_delete=models.CASCADE)

    # user = models.User...
    # labels = models.ManyToManyField

    @property
    def edit_url(self):
        return reverse('edit_contact_name', kwargs={"contact_id": self.pk})

    @property
    def photo_url(self):
        return self.photo.url if self.photo else None
