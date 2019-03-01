from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .authentication.urls import auth_router
from .edu.urls import edu_router
from .works.urls import works_router

schema_view = get_schema_view(
    openapi.Info(
        title="Athena API",
        default_version="v1",
        description="Athena service API endpoints",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class ContainerRouter(DefaultRouter):
    """Router class that collect all urls from other apps routers"""

    def register_router(self, router):
        self.registry.extend(router.registry)


root_router = ContainerRouter()
root_router.register_router(auth_router)
root_router.register_router(edu_router)
root_router.register_router(works_router)

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("", RedirectView.as_view(pattern_name="schema-redoc")),
]

urlpatterns += root_router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
