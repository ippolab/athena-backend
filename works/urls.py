from django.urls import path
from rest_framework import routers

from works.views import (
    ReportViewSet,
    TaskViewSet,
    attachment_view,
    document_view,
    templates_view,
)

works_router = routers.DefaultRouter()
works_router.register("reports", ReportViewSet)
works_router.register("tasks", TaskViewSet)

urlpatterns = [
    path(r"tasks/<int:pk>/<path:filename>", templates_view),
    path(r"reports/<int:pk>/<path:filename>", document_view),
    path(r"reports/<int:pk>/<path:filename>", attachment_view),
]
