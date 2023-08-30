from django.urls import path

from apps.users.views import (UserRegisterView, EmailConfirmationSentView,
                              UserConfirmEmailView, EmailConfirmedView,
                              EmailConfirmationFalideView)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("email-confirmation-sent/", EmailConfirmationSentView.as_view(),
         name="email_confirmation_sent"),
    path("confirm-email/<str:uidb64>/<str:token>/",
         UserConfirmEmailView.as_view(), name="confirm_email"),
    path("email-confirmed/", EmailConfirmedView.as_view(), name="email_confirmed"),
    path("confirm-email-failed/", EmailConfirmationFalideView.as_view(),
         name="email_confirmation_failed"),
]
