from django.urls import path
from rest_framework import routers

from athena.works.models import Task, Report
from .views import ReportViewSet, TaskViewSet, document_view

router = routers.DefaultRouter()
router.register("reports", ReportViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("tasks/<uuid:pk>/<str:document>", document_view(Task)),
    path("reports/<uuid:pk>/<str:document>", document_view(Report)),
]

urlpatterns += router.urls
