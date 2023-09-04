from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_message(user, url_name, subject, message):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_url = reverse_lazy(url_name, kwargs={'uidb64': uid,
                                                    'token': token})
    current_site = Site.objects.get_current().domain
    if current_site == 'example.com':
        current_site = '127.0.0.1:8000'
    send_mail(subject=subject,
              message=message + f'http://{current_site}{activation_url}',
              recipient_list=[user.email], from_email='vvglvv1@yandex.ru',
              fail_silently=False)
    print("Сообщение отправлено")
