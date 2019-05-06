from rest_framework import viewsets

from athena.authentication.permissions import IsAdmin, IsTeacher, IsTutor
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
    permission_classes = (IsTutor | IsTeacher | IsAdmin,)


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    permission_classes = (IsTutor | IsTeacher | IsAdmin,)


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = (IsTutor | IsTeacher | IsAdmin,)
