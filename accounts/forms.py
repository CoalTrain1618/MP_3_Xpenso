from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Extends UserCreationForm to make email required. This is a custom version of StackOverflow solution.
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required')

    class Mets:
        model = User
        fields = ('username', 'email', 'password1', 'password2')