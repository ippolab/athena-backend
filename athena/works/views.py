import uuid

from django.http import FileResponse, Http404, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from athena.authentication.permissions import (
    IsAdmin,
    IsTeacher,
    IsTutor,
    IsStudentAndReadOnly,
    IsStudent,
)
from .serializers import (
    Report,
    Task,
    TaskSerializer,
    ReportSerializer,
    ReportInTutorRequestSerializer,
    ReportInStudentRequestSerializer,
    ReportInCreateSerializer,
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
    permission_classes = (IsStudent | IsTutor | IsTeacher | IsAdmin,)

    def create(self, request):
        if str(request.user.id) == request.data.get("student") or request.user.is_admin:
            return super().create(request)

        return HttpResponseBadRequest()

    def get_queryset(self):
        user = self.request.user
        if user.is_only_student:
            return user.student.reports.all()
        return self.queryset

    def get_serializer_class(self):
        user = self.request.user
        if self.request.method in ("PUT", "PATCH"):
            if "status" in self.request.data and (user.is_tutor or user.is_teacher):
                return ReportInTutorRequestSerializer
            elif user.is_only_student:
                return ReportInStudentRequestSerializer
            else:
                return self.serializer_class

        elif self.request.method == "POST" and not user.is_admin:
            return ReportInCreateSerializer

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


@api_view(["GET"])
def report_from_task_view(request: Request, task_pk: uuid):
    if request.user.is_student:
        report = get_object_or_404(Report, task=task_pk, student__id=request.user.id)
    else:
        raise Http404()

    serializer = ReportSerializer(report)
    return Response(data=serializer.data)
