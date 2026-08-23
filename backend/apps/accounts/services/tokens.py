from django.conf import settings

from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def create_token_pair(user) -> dict[str, str]:
    """
    Create access and refresh JWT tokens for a user.
    """

    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


def refresh_token_pair(
    refresh_token: str,
) -> dict[str, str]:
    """
    Refresh access token.

    Because ROTATE_REFRESH_TOKENS=True,
    SimpleJWT may also return a new refresh token.
    """

    serializer = TokenRefreshSerializer(
        data={
            "refresh": refresh_token,
        }
    )

    serializer.is_valid(
        raise_exception=True
    )

    data = serializer.validated_data

    return {
        "access": str(data["access"]),
        "refresh": str(
            data.get(
                "refresh",
                refresh_token,
            )
        ),
    }


def blacklist_refresh_token(
    refresh_token: str,
) -> None:
    """
    Blacklist refresh token during logout.
    """

    token = RefreshToken(
        refresh_token
    )

    token.blacklist()


def set_auth_cookies(
    response,
    *,
    access_token: str,
    refresh_token: str,
):
    """
    Store JWT tokens inside HttpOnly cookies.
    """

    response.set_cookie(
        key=settings.JWT_ACCESS_COOKIE,
        value=access_token,
        max_age=settings.JWT_ACCESS_COOKIE_MAX_AGE,
        httponly=settings.JWT_COOKIE_HTTPONLY,
        secure=settings.JWT_COOKIE_SECURE,
        samesite=settings.JWT_COOKIE_SAMESITE,
        domain=settings.JWT_COOKIE_DOMAIN,
        path=settings.JWT_ACCESS_COOKIE_PATH,
    )

    response.set_cookie(
        key=settings.JWT_REFRESH_COOKIE,
        value=refresh_token,
        max_age=settings.JWT_REFRESH_COOKIE_MAX_AGE,
        httponly=settings.JWT_COOKIE_HTTPONLY,
        secure=settings.JWT_COOKIE_SECURE,
        samesite=settings.JWT_COOKIE_SAMESITE,
        domain=settings.JWT_COOKIE_DOMAIN,
        path=settings.JWT_REFRESH_COOKIE_PATH,
    )

    return response


def clear_auth_cookies(response):
    """
    Remove authentication cookies.
    """

    response.delete_cookie(
        key=settings.JWT_ACCESS_COOKIE,
        path=settings.JWT_ACCESS_COOKIE_PATH,
        domain=settings.JWT_COOKIE_DOMAIN,
        samesite=settings.JWT_COOKIE_SAMESITE,
    )

    response.delete_cookie(
        key=settings.JWT_REFRESH_COOKIE,
        path=settings.JWT_REFRESH_COOKIE_PATH,
        domain=settings.JWT_COOKIE_DOMAIN,
        samesite=settings.JWT_COOKIE_SAMESITE,
    )

    return response
