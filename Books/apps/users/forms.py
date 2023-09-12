from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    AuthenticationForm, SetPasswordForm
from django.utils.translation import gettext

from apps.users.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(
        label=gettext("Почта"),
        widget=forms.EmailInput(attrs={"class": "form-input"}),
        required=True
    )
    password1 = forms.CharField(
        label=gettext("Пароль"),
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
        required=True
    )
    password2 = forms.CharField(
        label=gettext("Повтор пароля"),
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('email',)
        field_order = ['email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    password = forms.CharField(
        label=gettext("Пароль"),
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = CustomUser
        fields = ('email',)


class ChangePasswordForm(SetPasswordForm):
    old_password = forms.CharField(
        label=gettext("Старый пароль"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(
        label=gettext("Новый пароль"),
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    new_password2 = forms.CharField(
        label=gettext("Подтверждение нового пароля"),
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class SaveUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']


class SaveProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phoneNumber', 'birth_date', 'country', 'city', 'id']
