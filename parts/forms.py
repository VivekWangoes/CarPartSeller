from .models import Contact
from django import forms

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"