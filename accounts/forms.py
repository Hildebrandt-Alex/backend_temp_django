from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Diese E-Mail-Adresse wird bereits verwendet.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        validate_password(password)  # nutzt Django's Passwort-Validatoren
        return password

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")