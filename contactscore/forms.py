from django import forms

from contactscore.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone_number", "email"]
