from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from .serializers import Report, ReportSerializer, Task, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def task_file_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return FileResponse(open(task.file.path, "rb"))


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def task_attachment_view(request: Request, pk):
    task = get_object_or_404(Task, pk=pk)
    return FileResponse(open(task.attachment.path, "rb"))


# todo set permissions to IsAdminOrOwner
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def report_file_view(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return FileResponse(open(report.file.path, "rb"))


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def report_attachment_view(request: Request, pk):
    report = get_object_or_404(Report, pk=pk)
    return FileResponse(open(report.attachment.path, "rb"))
