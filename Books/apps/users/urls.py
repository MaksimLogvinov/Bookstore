from django.urls import path

from apps.users.views import (RegisterUserView, EmailConfirmationSentView,
                              UserConfirmEmailView, EmailConfirmedView,
                              EmailConfirmationFailedView, LoginUserView,
                              ResetPasswordView, ResetPasswordDone,
                              ProfileUserView, logout_user,
                              EmailResetPasswordView, ResetPasswordFailed)


urlpatterns = [
    path("register/", RegisterUserView.as_view(),
         name="register"),
    path("email-confirmation-sent/", EmailConfirmationSentView.as_view(),
         name="email_confirmation_sent"),
    path("confirm-email/<str:uidb64>/<str:token>/",
         UserConfirmEmailView.as_view(),
         name="confirm_email"),
    path("password-email/<str:uidb64>/<str:token>/",
         EmailResetPasswordView.as_view(),
         name='password_email'),
    path("email-confirmed/", EmailConfirmedView.as_view(),
         name="email_confirmed"),
    path("confirm-email-failed/", EmailConfirmationFailedView.as_view(),
         name="email_confirmation_failed"),
    path("login/", LoginUserView.as_view(),
         name="login"),
    path("profile/", ProfileUserView.as_view(),
         name="profile_user"),
    path("logout/", logout_user,
         name='logout'),
    path("reset-password/", ResetPasswordView.as_view(),
         name="reset_password"),
    path("reset-password-done/", ResetPasswordDone.as_view(),
         name="password_confirmed"),
    path("reset-password-failed/", ResetPasswordFailed.as_view(),
         name="password_confirmation_failed"),
]
