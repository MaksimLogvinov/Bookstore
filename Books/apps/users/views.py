from gettext import gettext

from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView

from apps.users.forms import UserRegisterForm, LoginUserForm, \
    ChangePasswordForm, SaveUserForm, SaveProfileForm
from apps.users.models import CustomUser, Profile
from apps.users.services import send_message


class LoginUserView(LoginView):
    template_name = "users/login/login_user.html"
    form_class = LoginUserForm

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect('home_page')


class ProfileUserView(CreateView):
    template_name = "users/profile_user.html"
    model = Profile
    fields = SaveUserForm

    def get_context_data(self, **kwargs):
        context = {'title': 'Информация о пользователе'}
        return context

    def post(self, request, *args, **kwargs):
        form_data = SaveUserForm(request.POST)
        form_data2 = SaveProfileForm(request.POST)
        form_data.is_valid()
        form_data2.is_valid()
        CustomUser.objects.filter(
            id=request.user.id
        ).update(**form_data.cleaned_data)
        Profile.objects.filter(
            username_id_id=request.user.id
        ).update(**form_data2.cleaned_data)

        return redirect('security_user')


class SecurityUserView(ListView):
    model = CustomUser
    template_name = "users/security_user.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext("Безопасность и вход")

    @staticmethod
    def post(request):
        user = CustomUser.objects.get(email=request.user.email)
        user.delete()
        return redirect('home_page')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home_page')


User = get_user_model()


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_page')
    template_name = 'users/registration/user_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Регистрация на сайте')
        return context

    def form_valid(self, form):
        user = CustomUser.objects.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        send_message(
            user=user,
            url_name='confirm_email',
            subject=gettext('Подтвердите свой электронный адрес'),
            message=gettext('Пожалуйста, перейдите по следующей ссылке, '
                            'чтобы подтвердить свой адрес электронный почты:'))
        return redirect('email_confirmation_sent')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user,
                                                                    token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('profile_user')
        else:
            return redirect('email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/registration/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Письмо активации отправлено')
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/registration/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Ваш электронный адрес не активирован')
        return context


class ResetPasswordView(TemplateView):
    template_name = 'users/login/login_user.html'
    form_class = ChangePasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Изменение пароля')
        return context

    def post(self, request):
        send_message(
            user=self.request.user,
            url_name='password_email',
            subject=gettext('Ваш пароль пытаются сменить'),
            message=gettext('Перейдите по следующей ссылке, '
                            'чтобы сменить пароль:'))
        return redirect('email_confirmation_sent')


class EmailResetPasswordView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user,
                                                                    token):
            return redirect('password_confirmed')
        else:
            return redirect('password_confirmation_failed')


class ResetPasswordDone(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "users/password/password_confirmed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Успешно')
        return context

    def form_valid(self, form):
        if (form.cleaned_data['new_password1'] == form.cleaned_data['new_password2']):
            user = CustomUser.objects.get(email=self.request.user.email)
            user.set_password(str(form.cleaned_data['new_password1']))
            print(form.cleaned_data['new_password1'])
            user.save()
        return redirect('home_page')


class ResetPasswordFailed(TemplateView):
    template_name = 'users/registration/password_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext(
            'Ваш пароль не был сменён, повторите попытку')
        return context
