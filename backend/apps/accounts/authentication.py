from django.conf import settings

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import SAFE_METHODS
from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    """
    JWT authentication using an HttpOnly access-token cookie.

    Safe requests:
        GET, HEAD, OPTIONS
        -> JWT validation only

    Unsafe requests:
        POST, PUT, PATCH, DELETE
        -> JWT validation + CSRF validation
    """

    def authenticate(self, request):
        raw_token = request.COOKIES.get(
            settings.JWT_ACCESS_COOKIE
        )

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)

        if request.method not in SAFE_METHODS:
            SessionAuthentication().enforce_csrf(request)

        return user, validated_token
