from django import forms

from contactscore.models import Contact, ContactBook


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone_number", "email", "photo"]

class ContactBookForm(forms.ModelForm):
    class Meta:
        model = ContactBook
        fields = ["name", "description"]
