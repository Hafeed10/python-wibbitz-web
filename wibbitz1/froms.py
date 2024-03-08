from django.forms import ModeleForm
from wibbitz1.models import Contact
from django import forms


class ContactForm(forms.ModeleForm):
    class Meta:
        model = Contact
        fields = "_all_"