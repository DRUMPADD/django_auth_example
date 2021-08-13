from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CreateUser

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text="100 characters of fewer")

    class Meta:
        model = CreateUser
        fields = UserCreationForm.Meta.fields + ('full_name', 'age',)