from gettext import gettext

from django.contrib.auth import get_user_model, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, TemplateView

from apps.users.forms import UserRegisterForm


# from apps.users.services import verification


class LoginUser(CreateView):
    def get_context_data(self, **kwargs):
        context = {}
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # verification(user)


User = get_user_model()


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_page')
    template_name = 'users/registration/user_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Регистрация на сайте')
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('confirm_email', kwargs={'uidb64': uid,
                                                               'token': token})
        current_site = Site.objects.get_current().domain
        if current_site == 'example.com':
            current_site = '127.0.0.1:8000'
        send_mail(subject='Подтвердите свой электронный адрес',
                  message=f'Пожалуйста, перейдите по следующей ссылке,'
                          f' чтобы подтвердить свой адрес электронный почты:'
                          f' http://{current_site}{activation_url}, ',
                  recipient_list=[user.email], from_email='vvglvv1@yandex.ru',
                  fail_silently=False)

        return redirect('email_confirmation_sent')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('email_confirmed')
        else:
            return redirect('email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'users/registration/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Письмо активации отправлено')
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'users/registration/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Ваш электронный адрес активирован')
        return context


class EmailConfirmationFalideView(TemplateView):
    template_name = 'users/registration/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext('Ваш электронный адрес не активирован')
        return context
