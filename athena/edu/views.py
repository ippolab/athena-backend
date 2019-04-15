from rest_framework import viewsets

from athena.authentication.permissions import IsAdmin, IsTutor, IsTeacher
from .serializers import (
    Speciality,
    SpecialitySerializer,
    StudentGroup,
    StudentGroupSerializer,
    Subject,
    SubjectSerializer,
)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (IsAdmin | IsTutor | IsTeacher,)


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = (IsAdmin | IsTutor | IsTeacher,)


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (IsAdmin | IsTutor | IsTeacher,)
