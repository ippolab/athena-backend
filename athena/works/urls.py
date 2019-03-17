from django.urls import path
from rest_framework import routers

from .views import (
    ReportViewSet,
    TaskViewSet,
    attachment_view,
    document_view,
    templates_view,
)

router = routers.DefaultRouter()
router.register("reports", ReportViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [
    path(r"tasks/<uuid:pk>/<path:filename>", templates_view),
    path(r"reports/<uuid:pk>/<path:filename>", document_view),
    path(r"reports/<uuid:pk>/<path:filename>", attachment_view),
]

urlpatterns += router.urls

