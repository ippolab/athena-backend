from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request

from athena.authentication.permissions import (
    IsAdmin,
    IsTeacher,
    IsTutor,
    IsStudentAndReadOnly,
    IsStudentAndOwner,
)
from .serializers import Report, ReportInCreateSerializer, Task, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsStudentAndReadOnly | IsTutor | IsTeacher | IsAdmin,)

    def get_queryset(self):
        user = self.request.user
        if user.is_only_student:
            return Task.objects.filter(student_group=user.student.student_group)
        return self.queryset


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportInCreateSerializer  # todo
    permission_classes = (IsStudentAndOwner | IsTutor | IsTeacher | IsAdmin,)

    def get_queryset(self):
        user = self.request.user
        if user.is_only_student:
            return user.student.reports.all()
        return self.queryset


def document_view(model):
    @api_view(["GET"])
    def view(request: Request, pk, document: str):
        if request.user.is_only_student:
            report = get_object_or_404(model, pk=pk, student=request.user)
        else:
            report = get_object_or_404(model, pk=pk)
        if document == "file":
            document = report.file
        elif document == "attachment":
            document = report.attachment
        else:
            raise Http404()
        if document:
            return FileResponse(open(document.path, "rb"))
        raise Http404()

    return view
