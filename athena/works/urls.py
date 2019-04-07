from django.urls import path
from rest_framework import routers

from .views import (
    ReportViewSet,
    TaskViewSet,
    report_attachment_view,
    report_file_view,
    task_attachment_view,
    task_file_view,
)

router = routers.DefaultRouter()
router.register("reports", ReportViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("tasks/<uuid:pk>/file", task_file_view),
    path("tasks/<uuid:pk>/attachment", task_attachment_view),
    path("reports/<uuid:pk>/file", report_file_view),
    path("reports/<uuid:pk>/attachment", report_attachment_view),
]

urlpatterns += router.urls
