from django.urls import path

from apps.accounts.api.views import (
    CSRFView,
    ChangePasswordView,
    LoginView,
    LogoutView,
    MeView,
    RefreshView,
    RegisterView,
    ResendVerificationView,
    VerifyEmailView,
)


app_name = "accounts"


urlpatterns = [
    # CSRF
    path(
        "auth/csrf/",
        CSRFView.as_view(),
        name="csrf",
    ),

    # Registration
    path(
        "auth/register/",
        RegisterView.as_view(),
        name="register",
    ),

    # Email verification
    path(
        "auth/verify-email/",
        VerifyEmailView.as_view(),
        name="verify-email",
    ),

    path(
        "auth/resend-verification/",
        ResendVerificationView.as_view(),
        name="resend-verification",
    ),

    # Authentication
    path(
        "auth/login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "auth/refresh/",
        RefreshView.as_view(),
        name="refresh",
    ),

    path(
        "auth/logout/",
        LogoutView.as_view(),
        name="logout",
    ),

    # Current user
    path(
        "me/",
        MeView.as_view(),
        name="me",
    ),

    path(
        "me/change-password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
]
