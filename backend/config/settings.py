import os
from datetime import timedelta
from pathlib import Path


# =============================================================================
# Paths
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================================================================
# Environment helpers
# =============================================================================

def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)

    if value is None:
        return default

    return value.lower() in {
        "1",
        "true",
        "yes",
        "on",
    }


def env_list(name: str, default: str = "") -> list[str]:
    return [
        item.strip()
        for item in os.getenv(name, default).split(",")
        if item.strip()
    ]


# =============================================================================
# Core
# =============================================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "unsafe-development-secret-key",
)

DEBUG = env_bool(
    "DJANGO_DEBUG",
    False,
)

ALLOWED_HOSTS = env_list(
    "DJANGO_ALLOWED_HOSTS",
    "localhost,127.0.0.1,backend",
)


# =============================================================================
# Applications
# =============================================================================

INSTALLED_APPS = [
    # -------------------------------------------------------------------------
    # Django
    # -------------------------------------------------------------------------
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # -------------------------------------------------------------------------
    # Third-party
    # -------------------------------------------------------------------------
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
    "corsheaders",
    "django_filters",

    # -------------------------------------------------------------------------
    # Local apps
    # -------------------------------------------------------------------------
    "apps.accounts.apps.AccountsConfig",
    "apps.blog.apps.BlogConfig",
]


# =============================================================================
# Middleware
# =============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # CORS middleware باید قبل از CommonMiddleware باشد
    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    # برای CSRF protection
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =============================================================================
# URL / WSGI
# =============================================================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# =============================================================================
# Templates
# =============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =============================================================================
# Database - PostgreSQL
# =============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",

        "NAME": os.getenv(
            "POSTGRES_DB",
            "fullstack_lab",
        ),

        "USER": os.getenv(
            "POSTGRES_USER",
            "fullstack_user",
        ),

        "PASSWORD": os.getenv(
            "POSTGRES_PASSWORD",
            "",
        ),

        # داخل Docker اسم سرویس PostgreSQL ما db است
        "HOST": os.getenv(
            "POSTGRES_HOST",
            "db",
        ),

        # داخل شبکه Docker همیشه PostgreSQL روی 5432 است
        "PORT": os.getenv(
            "POSTGRES_INTERNAL_PORT",
            "5432",
        ),

        # اتصال‌ها برای مدت کوتاهی reuse شوند
        "CONN_MAX_AGE": 60,

        # قبل از reuse شدن connection سلامت آن بررسی شود
        "CONN_HEALTH_CHECKS": True,
    }
}


# =============================================================================
# Custom User
# =============================================================================

AUTH_USER_MODEL = "accounts.User"


# =============================================================================
# Password validation
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =============================================================================
# Internationalization
# =============================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =============================================================================
# Static files
# =============================================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# =============================================================================
# Media / Uploads
# =============================================================================
# برای:
# - عکس پست‌های Blog
# - عکس پروفایل
# - فایل‌های آپلودی آینده

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =============================================================================
# Django REST Framework
# =============================================================================

REST_FRAMEWORK = {
    # -------------------------------------------------------------------------
    # Authentication
    # -------------------------------------------------------------------------
    # JWT را از HttpOnly Cookie می‌خوانیم
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "apps.accounts.authentication.CookieJWTAuthentication",
    ),

    # -------------------------------------------------------------------------
    # Permissions
    # -------------------------------------------------------------------------
    # Secure by default
    #
    # یعنی تمام APIها به صورت پیش‌فرض Login می‌خواهند.
    # endpointهای عمومی بعداً صریحاً AllowAny خواهند داشت.
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),

    # -------------------------------------------------------------------------
    # OpenAPI / Swagger
    # -------------------------------------------------------------------------
    "DEFAULT_SCHEMA_CLASS": (
        "drf_spectacular.openapi.AutoSchema"
    ),

    # -------------------------------------------------------------------------
    # Filtering
    # -------------------------------------------------------------------------
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
}


# =============================================================================
# Simple JWT
# =============================================================================

SIMPLE_JWT = {
    # Access token کوتاه‌مدت
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=15,
    ),

    # Refresh token بلندمدت‌تر
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=7,
    ),

    # هنگام Refresh یک Refresh Token جدید بساز
    "ROTATE_REFRESH_TOKENS": True,

    # Refresh Token قبلی بعد از rotation باطل شود
    "BLACKLIST_AFTER_ROTATION": True,

    # فعلاً last_login را با هر login تغییر نمی‌دهیم
    "UPDATE_LAST_LOGIN": False,

    # اگر جایی در آینده Authorization Header هم استفاده کردیم
    "AUTH_HEADER_TYPES": (
        "Bearer",
    ),
}


# =============================================================================
# JWT Cookies
# =============================================================================

JWT_ACCESS_COOKIE = "access_token"

JWT_REFRESH_COOKIE = "refresh_token"


# -----------------------------------------------------------------------------
# Cookie lifetime
# -----------------------------------------------------------------------------

JWT_ACCESS_COOKIE_MAX_AGE = (
    15 * 60
)

JWT_REFRESH_COOKIE_MAX_AGE = (
    7 * 24 * 60 * 60
)


# -----------------------------------------------------------------------------
# HttpOnly
# -----------------------------------------------------------------------------
# JavaScript / React نمی‌تواند JWT را بخواند.

JWT_COOKIE_HTTPONLY = True


# -----------------------------------------------------------------------------
# Secure
# -----------------------------------------------------------------------------
# Development:
# False
#
# Production + HTTPS:
# True

JWT_COOKIE_SECURE = env_bool(
    "JWT_COOKIE_SECURE",
    False,
)


# -----------------------------------------------------------------------------
# SameSite
# -----------------------------------------------------------------------------

JWT_COOKIE_SAMESITE = os.getenv(
    "JWT_COOKIE_SAMESITE",
    "Lax",
)


# -----------------------------------------------------------------------------
# Domain
# -----------------------------------------------------------------------------
# در development نیاز نداریم.
# بعداً برای production قابل تنظیم است.

JWT_COOKIE_DOMAIN = (
    os.getenv("JWT_COOKIE_DOMAIN")
    or None
)


# -----------------------------------------------------------------------------
# Cookie paths
# -----------------------------------------------------------------------------

# Access token باید روی تمام API قابل ارسال باشد.
JWT_ACCESS_COOKIE_PATH = "/"


# Refresh token فقط برای endpointهای auth لازم است.
JWT_REFRESH_COOKIE_PATH = "/api/auth/"


# =============================================================================
# CSRF
# =============================================================================
# JWT داخل HttpOnly Cookie است.
#
# ولی CSRF token باید توسط React قابل خواندن باشد
# تا React بتواند در درخواست‌های unsafe آن را بفرستد:
#
# X-CSRFToken: ...


CSRF_COOKIE_HTTPONLY = False


CSRF_COOKIE_SECURE = JWT_COOKIE_SECURE


CSRF_COOKIE_SAMESITE = JWT_COOKIE_SAMESITE


CSRF_TRUSTED_ORIGINS = env_list(
    "CSRF_TRUSTED_ORIGINS",
    (
        "http://localhost:5173,"
        "http://127.0.0.1:5173"
    ),
)


# =============================================================================
# CORS
# =============================================================================

CORS_ALLOWED_ORIGINS = env_list(
    "CORS_ALLOWED_ORIGINS",
    (
        "http://localhost:5173,"
        "http://127.0.0.1:5173"
    ),
)


# React اجازه دارد Cookie را همراه request ارسال کند
CORS_ALLOW_CREDENTIALS = True


# =============================================================================
# Django Session Cookies
# =============================================================================
# Django Admin همچنان از Session Authentication استفاده می‌کند.

SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = JWT_COOKIE_SECURE

SESSION_COOKIE_SAMESITE = JWT_COOKIE_SAMESITE


# =============================================================================
# Swagger / OpenAPI
# =============================================================================

SPECTACULAR_SETTINGS = {
    "TITLE": "Fullstack Lab API",

    "DESCRIPTION": (
        "Backend API for Fullstack Lab"
    ),

    "VERSION": "1.0.0",

    # schema endpoint داخل خود Swagger نمایش داده نشود
    "SERVE_INCLUDE_SCHEMA": False,

    # نام componentها تمیزتر بماند
    "COMPONENT_SPLIT_REQUEST": True,
}


# =============================================================================
# Email
# =============================================================================
# فعلاً Development:
#
# ایمیل واقعی ارسال نمی‌شود.
# متن ایمیل داخل terminal چاپ می‌شود.
#
# بعداً SMTP واقعی:
# Gmail / Mailgun / Brevo / SES / ...
# را فقط با Environment Variables تنظیم می‌کنیم.


EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    "noreply@localhost",
)


# =============================================================================
# Security defaults
# =============================================================================

X_FRAME_OPTIONS = "DENY"

SECURE_CONTENT_TYPE_NOSNIFF = True


# =============================================================================
# Default primary key
# =============================================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
