from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
