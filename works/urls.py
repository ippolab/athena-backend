from django.urls import path
from rest_framework import routers

from works.views import download_document, download_source, TaskViewSet, ReportViewSet

works_router = routers.DefaultRouter()
works_router.register('reports', ReportViewSet)
works_router.register('tasks', TaskViewSet)

urlpatterns = [
    path('reports-document/<pk>/', download_document),
    path('reports-attachment/<pk>/', download_source)

]
