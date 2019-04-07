from rest_framework import viewsets

from .serializers import (
    StudentGroup,
    Speciality,
    StudentGroupSerializer,
    Subject,
    SubjectSerializer,
    SpecialitySerializer)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
