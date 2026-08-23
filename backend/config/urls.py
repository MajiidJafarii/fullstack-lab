from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
    # -------------------------------------------------------------------------
    # Django Admin
    # -------------------------------------------------------------------------
    path(
        "admin/",
        admin.site.urls,
    ),

    # -------------------------------------------------------------------------
    # Application API
    # -------------------------------------------------------------------------
    path(
        "api/",
        include(
            "apps.accounts.api.urls"
        ),
    ),

    # -------------------------------------------------------------------------
    # OpenAPI Schema
    # -------------------------------------------------------------------------
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    # -------------------------------------------------------------------------
    # Swagger UI
    # -------------------------------------------------------------------------
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]


# Development only
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
