from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import Task, TaskSerializer, Report, ReportSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


def download_document(request, pk):
    report = get_object_or_404(Report, pk=pk)
    document = report.document.open()
    response = HttpResponse(
        document,
        content_type='application/pdf'
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(document.name)
    return response


def download_source(request, pk):
    report = get_object_or_404(Report, pk=pk)
    file = report.attachment.open()
    response = HttpResponse(
        file,
        content_type='application/zip'
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response
