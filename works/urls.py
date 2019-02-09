from django.urls import path
from rest_framework import routers

from works.views import document_view, attachment_view, TaskViewSet, ReportViewSet, templates_view

works_router = routers.DefaultRouter()
works_router.register('reports', ReportViewSet)
works_router.register('tasks', TaskViewSet)

urlpatterns = [
    path(r'tasks/<int:pk>/<path:filename>', templates_view),
    path(r'reports/<int:pk>/<path:filename>', document_view),
    path(r'reports/<int:pk>/<path:filename>', attachment_view)

]
