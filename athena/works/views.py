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
    IsOwner,
    IsStudent)
from .serializers import (
    Report,
    Task,
    TaskSerializer,
    ReportSerializer,
    ReportInTutorRequestSerializer,
    ReportInStudentRequestSerializer,
)


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
    serializer_class = ReportSerializer
    permission_classes = ((IsStudent & IsOwner) | IsTutor | IsTeacher | IsAdmin,)

    def get_queryset(self):
        user = self.request.user
        if user.is_only_student:
            return user.student.reports.all()
        return self.queryset

    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT", "PATCH"):
            if "status" in self.request.data and not self.request.user.is_only_student:
                return ReportInTutorRequestSerializer
            else:
                return ReportInStudentRequestSerializer
        return self.serializer_class


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
