from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from works.storage import compare_dirs
from .serializers import Task, TaskSerializer, Report, ReportSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


def download_file(file, content_type: str) -> HttpResponse:
    response = HttpResponse(
        file,
        content_type='application/{}'.format(content_type)
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file.name)
    return response


def templates_view(request, pk, filename):
    task = get_object_or_404(Task, pk=pk)

    if compare_dirs(task.templates.path, filename):
        file = task.templates.open()
        return download_file(file, 'zip')

    return HttpResponse(status=404)


def document_view(request, pk, filename):
    report = get_object_or_404(Report, pk=pk)

    if compare_dirs(report.document.path, filename):
        document = report.document.open()
        return download_file(document, 'pdf')
    return HttpResponse(status=404)


def attachment_view(request, pk, filename):
    report = get_object_or_404(Report, pk=pk)
    if compare_dirs(report.attachment.path, filename):
        file = report.attachment.open()
        return download_file(file, 'zip')
    return HttpResponse(status=404)
