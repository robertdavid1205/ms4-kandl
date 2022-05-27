from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form to collect contact form details
    """
    class Meta:
        model = Contact
        fields = "__all__"
