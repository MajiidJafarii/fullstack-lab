import re

from django.core import mail
from django.test import override_settings

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.accounts.models import EmailVerificationCode, User


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
)
class AuthAPITests(APITestCase):
    """
    Tests for the complete authentication flow:

    CSRF
    -> Register
    -> Email verification
    -> Login
    -> HttpOnly cookies
    -> Me
    -> Refresh
    -> Logout
    """

    def setUp(self):
        self.client = APIClient(
            enforce_csrf_checks=True
        )

        self.email = "user@example.com"
        self.password = "StrongPass!9347"

    # =========================================================================
    # Helpers
    # =========================================================================

    def get_csrf_token(self):
        response = self.client.get(
            "/api/auth/csrf/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "csrfToken",
            response.data,
        )

        return response.data[
            "csrfToken"
        ]

    def register_user(self):
        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/register/",
            {
                "email": self.email,
                "first_name": "Test",
                "last_name": "User",
                "password": self.password,
                "password_confirm": self.password,
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        return response

    def get_verification_code_from_email(self):
        self.assertEqual(
            len(mail.outbox),
            1,
        )

        email = mail.outbox[-1]

        self.assertEqual(
            email.to,
            [self.email],
        )

        match = re.search(
            r"\b\d{6}\b",
            email.body,
        )

        self.assertIsNotNone(
            match,
            "No 6-digit verification code found in email.",
        )

        return match.group(0)

    def verify_user(self):
        code = (
            self.get_verification_code_from_email()
        )

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/verify-email/",
            {
                "email": self.email,
                "code": code,
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        return response

    def login_user(self):
        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/login/",
            {
                "email": self.email,
                "password": self.password,
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        return response

    def create_verified_and_logged_in_user(self):
        self.register_user()
        self.verify_user()
        return self.login_user()

    # =========================================================================
    # CSRF
    # =========================================================================

    def test_csrf_endpoint_returns_token(self):
        response = self.client.get(
            "/api/auth/csrf/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "csrfToken",
            response.data,
        )

        self.assertIn(
            "csrftoken",
            response.cookies,
        )

    def test_register_without_csrf_is_rejected(self):
        response = self.client.post(
            "/api/auth/register/",
            {
                "email": self.email,
                "password": self.password,
                "password_confirm": self.password,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    # =========================================================================
    # Register
    # =========================================================================

    def test_register_creates_inactive_unverified_user(self):
        self.register_user()

        user = User.objects.get(
            email=self.email
        )

        self.assertFalse(
            user.is_active
        )

        self.assertFalse(
            user.email_verified
        )

        self.assertTrue(
            user.check_password(
                self.password
            )
        )

        self.assertFalse(
            user.is_superuser
        )

        self.assertFalse(
            user.is_staff
        )

    def test_register_sends_verification_email(self):
        self.register_user()

        self.assertEqual(
            len(mail.outbox),
            1,
        )

        email = mail.outbox[0]

        self.assertEqual(
            email.to,
            [self.email],
        )

        code = (
            self.get_verification_code_from_email()
        )

        self.assertEqual(
            len(code),
            6,
        )

        self.assertTrue(
            code.isdigit()
        )

    def test_verification_code_is_not_stored_as_plain_text(self):
        self.register_user()

        raw_code = (
            self.get_verification_code_from_email()
        )

        verification = (
            EmailVerificationCode.objects.get()
        )

        self.assertNotEqual(
            verification.code_hash,
            raw_code,
        )

    def test_duplicate_email_cannot_register(self):
        self.register_user()

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/register/",
            {
                "email": self.email,
                "password": self.password,
                "password_confirm": self.password,
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

    # =========================================================================
    # Email verification
    # =========================================================================

    def test_verify_email_activates_user(self):
        self.register_user()

        self.verify_user()

        user = User.objects.get(
            email=self.email
        )

        self.assertTrue(
            user.email_verified
        )

        self.assertTrue(
            user.is_active
        )

        verification = (
            EmailVerificationCode.objects
            .filter(user=user)
            .latest("created_at")
        )

        self.assertIsNotNone(
            verification.used_at
        )

    def test_invalid_verification_code_is_rejected(self):
        self.register_user()

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/verify-email/",
            {
                "email": self.email,
                "code": "000000",
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        user = User.objects.get(
            email=self.email
        )

        self.assertFalse(
            user.email_verified
        )

        verification = (
            EmailVerificationCode.objects
            .filter(user=user)
            .latest("created_at")
        )

        self.assertEqual(
            verification.attempts,
            1,
        )

    # =========================================================================
    # Login
    # =========================================================================

    def test_unverified_user_cannot_login(self):
        self.register_user()

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/login/",
            {
                "email": self.email,
                "password": self.password,
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_verified_user_can_login(self):
        self.register_user()
        self.verify_user()

        response = self.login_user()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["user"]["email"],
            self.email,
        )

    def test_login_sets_httponly_jwt_cookies(self):
        self.register_user()
        self.verify_user()

        response = self.login_user()

        self.assertIn(
            "access_token",
            response.cookies,
        )

        self.assertIn(
            "refresh_token",
            response.cookies,
        )

        access_cookie = response.cookies[
            "access_token"
        ]

        refresh_cookie = response.cookies[
            "refresh_token"
        ]

        self.assertTrue(
            access_cookie["httponly"]
        )

        self.assertTrue(
            refresh_cookie["httponly"]
        )

    def test_wrong_password_is_rejected(self):
        self.register_user()
        self.verify_user()

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/login/",
            {
                "email": self.email,
                "password": "WrongPassword!123",
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    # =========================================================================
    # Me
    # =========================================================================

    def test_me_requires_authentication(self):
        response = self.client.get(
            "/api/me/"
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ],
        )

    def test_logged_in_user_can_get_me(self):
        self.create_verified_and_logged_in_user()

        response = self.client.get(
            "/api/me/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["email"],
            self.email,
        )

        self.assertTrue(
            response.data[
                "email_verified"
            ]
        )

    # =========================================================================
    # CSRF + authenticated unsafe request
    # =========================================================================

    def test_authenticated_patch_without_csrf_is_rejected(self):
        self.create_verified_and_logged_in_user()

        response = self.client.patch(
            "/api/me/",
            {
                "first_name": "Changed",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_authenticated_patch_with_csrf_works(self):
        self.create_verified_and_logged_in_user()

        csrf_token = self.get_csrf_token()

        response = self.client.patch(
            "/api/me/",
            {
                "first_name": "Majid",
                "last_name": "Jafari",
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        user = User.objects.get(
            email=self.email
        )

        self.assertEqual(
            user.first_name,
            "Majid",
        )

        self.assertEqual(
            user.last_name,
            "Jafari",
        )

    # =========================================================================
    # Refresh
    # =========================================================================

    def test_refresh_creates_new_access_token(self):
        self.create_verified_and_logged_in_user()

        old_access = self.client.cookies[
            "access_token"
        ].value

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/refresh/",
            {},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "access_token",
            response.cookies,
        )

        new_access = response.cookies[
            "access_token"
        ].value

        self.assertNotEqual(
            old_access,
            new_access,
        )

    # =========================================================================
    # Change password
    # =========================================================================

    def test_change_password(self):
        self.create_verified_and_logged_in_user()

        csrf_token = self.get_csrf_token()

        new_password = (
            "AnotherStrongPass!5278"
        )

        response = self.client.post(
            "/api/me/change-password/",
            {
                "current_password": self.password,
                "new_password": new_password,
                "new_password_confirm": new_password,
            },
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        user = User.objects.get(
            email=self.email
        )

        self.assertTrue(
            user.check_password(
                new_password
            )
        )

    # =========================================================================
    # Logout
    # =========================================================================

    def test_logout_clears_auth_cookies(self):
        self.create_verified_and_logged_in_user()

        self.assertIn(
            "access_token",
            self.client.cookies,
        )

        self.assertIn(
            "refresh_token",
            self.client.cookies,
        )

        csrf_token = self.get_csrf_token()

        response = self.client.post(
            "/api/auth/logout/",
            {},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_token,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn(
            "access_token",
            response.cookies,
        )

        self.assertIn(
            "refresh_token",
            response.cookies,
        )

        self.assertEqual(
            response.cookies[
                "access_token"
            ].value,
            "",
        )

        self.assertEqual(
            response.cookies[
                "refresh_token"
            ].value,
            "",
        )
