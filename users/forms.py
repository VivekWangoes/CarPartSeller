from .models import User
from django import forms


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone_no']