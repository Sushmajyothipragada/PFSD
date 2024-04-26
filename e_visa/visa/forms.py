from django import forms
from .models import Userregistration

class UserregistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userregistration
        field = "__all__"
        exclude = ["id"]