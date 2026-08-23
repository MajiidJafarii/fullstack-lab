from django.conf import settings
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from apps.accounts.api.serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    RegisterSerializer,
    ResendVerificationSerializer,
    UpdateProfileSerializer,
    UserSerializer,
    VerifyEmailSerializer,
)
from apps.accounts.models import User
from apps.accounts.services.email_verification import (
    EmailAlreadyVerifiedError,
    VerificationCodeAttemptsExceededError,
    VerificationCodeCooldownError,
    VerificationCodeExpiredError,
    VerificationCodeInvalidError,
    send_verification_code,
    verify_email_code,
)
from apps.accounts.services.tokens import (
    blacklist_refresh_token,
    clear_auth_cookies,
    create_token_pair,
    refresh_token_pair,
    set_auth_cookies,
)


# =============================================================================
# CSRF
# =============================================================================


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CSRFView(APIView):
    authentication_classes = []
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request):
        token = get_token(request)

        return Response(
            {
                "csrfToken": token,
            },
            status=status.HTTP_200_OK,
        )


# =============================================================================
# Register
# =============================================================================


@method_decorator(csrf_protect, name="dispatch")
class RegisterView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = serializer.save()

        send_verification_code(user)

        return Response(
            {
                "message": (
                    "Registration successful. "
                    "Please verify your email."
                ),
                "email": user.email,
            },
            status=status.HTTP_201_CREATED,
        )


# =============================================================================
# Verify email
# =============================================================================


@method_decorator(csrf_protect, name="dispatch")
class VerifyEmailView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = VerifyEmailSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        email = serializer.validated_data[
            "email"
        ]

        code = serializer.validated_data[
            "code"
        ]

        user = User.objects.filter(
            email__iexact=email,
        ).first()

        if user is None:
            return Response(
                {
                    "detail": (
                        "Invalid email or verification code."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            verify_email_code(
                user=user,
                code=code,
            )

        except VerificationCodeExpiredError as exc:
            return Response(
                {
                    "detail": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except VerificationCodeAttemptsExceededError as exc:
            return Response(
                {
                    "detail": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        except VerificationCodeInvalidError as exc:
            return Response(
                {
                    "detail": str(exc),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Email verified successfully."
                )
            },
            status=status.HTTP_200_OK,
        )


# =============================================================================
# Resend verification
# =============================================================================


@method_decorator(csrf_protect, name="dispatch")
class ResendVerificationView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = ResendVerificationSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        email = serializer.validated_data[
            "email"
        ]

        user = User.objects.filter(
            email__iexact=email,
        ).first()

        # برای جلوگیری از account enumeration،
        # چه کاربر وجود داشته باشد چه نداشته باشد،
        # پاسخ کلی برمی‌گردانیم.
        if user is None:
            return Response(
                {
                    "message": (
                        "If the account exists, "
                        "a verification code will be sent."
                    )
                },
                status=status.HTTP_200_OK,
            )

        try:
            send_verification_code(user)

        except EmailAlreadyVerifiedError:
            return Response(
                {
                    "message": (
                        "If the account exists, "
                        "a verification code will be sent."
                    )
                },
                status=status.HTTP_200_OK,
            )

        except VerificationCodeCooldownError as exc:
            return Response(
                {
                    "detail": str(exc),
                    "seconds_remaining": (
                        exc.seconds_remaining
                    ),
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        return Response(
            {
                "message": (
                    "If the account exists, "
                    "a verification code will be sent."
                )
            },
            status=status.HTTP_200_OK,
        )


# =============================================================================
# Login
# =============================================================================


@method_decorator(csrf_protect, name="dispatch")
class LoginView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        email = serializer.validated_data[
            "email"
        ]

        password = serializer.validated_data[
            "password"
        ]

        user = User.objects.filter(
            email__iexact=email,
        ).first()

        if (
            user is None
            or not user.check_password(password)
        ):
            return Response(
                {
                    "detail": (
                        "Invalid email or password."
                    )
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.email_verified:
            return Response(
                {
                    "detail": (
                        "Email verification is required."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        if not user.is_active:
            return Response(
                {
                    "detail": (
                        "This account is inactive."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        tokens = create_token_pair(user)

        response = Response(
            {
                "message": "Login successful.",
                "user": UserSerializer(
                    user
                ).data,
            },
            status=status.HTTP_200_OK,
        )

        set_auth_cookies(
            response,
            access_token=tokens["access"],
            refresh_token=tokens["refresh"],
        )

        return response


# =============================================================================
# Refresh
# =============================================================================


@method_decorator(csrf_protect, name="dispatch")
class RefreshView(APIView):
    authentication_classes = []
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request):
        refresh_token = request.COOKIES.get(
            settings.JWT_REFRESH_COOKIE
        )

        if not refresh_token:
            return Response(
                {
                    "detail": (
                        "Refresh token is missing."
                    )
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        try:
            tokens = refresh_token_pair(
                refresh_token
            )

        except (
            TokenError,
            DRFValidationError,
        ):
            response = Response(
                {
                    "detail": (
                        "Refresh token is invalid "
                        "or expired."
                    )
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

            clear_auth_cookies(
                response
            )

            return response

        response = Response(
            {
                "message": (
                    "Token refreshed successfully."
                )
            },
            status=status.HTTP_200_OK,
        )

        set_auth_cookies(
            response,
            access_token=tokens["access"],
            refresh_token=tokens["refresh"],
        )

        return response


# =============================================================================
# Logout
# =============================================================================


@method_decorator(csrf_protect, name="dispatch")
class LogoutView(APIView):
    # logout باید حتی اگر access token منقضی شده
    # باشد نیز قابل انجام باشد.
    authentication_classes = []

    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request):
        refresh_token = request.COOKIES.get(
            settings.JWT_REFRESH_COOKIE
        )

        if refresh_token:
            try:
                blacklist_refresh_token(
                    refresh_token
                )
            except TokenError:
                pass

        response = Response(
            {
                "message": (
                    "Logout successful."
                )
            },
            status=status.HTTP_200_OK,
        )

        clear_auth_cookies(
            response
        )

        return response


# =============================================================================
# Current user / Profile
# =============================================================================


class MeView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        serializer = UserSerializer(
            request.user
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def patch(self, request):
        serializer = UpdateProfileSerializer(
            request.user,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save()

        return Response(
            UserSerializer(
                request.user
            ).data,
            status=status.HTTP_200_OK,
        )


# =============================================================================
# Change password
# =============================================================================


class ChangePasswordView(
    generics.GenericAPIView
):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = (
        ChangePasswordSerializer
    )

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = request.user

        current_password = (
            serializer.validated_data[
                "current_password"
            ]
        )

        new_password = (
            serializer.validated_data[
                "new_password"
            ]
        )

        if not user.check_password(
            current_password
        ):
            return Response(
                {
                    "current_password": [
                        "Current password is incorrect."
                    ]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(
            new_password
        )

        user.save(
            update_fields=[
                "password",
            ]
        )

        return Response(
            {
                "message": (
                    "Password changed successfully."
                )
            },
            status=status.HTTP_200_OK,
        )
