from rest_framework import viewsets

from authentication.models import Student, Teacher, Tutor

from .serializers import (
    Group,
    GroupSerializer,
    StudentSerializer,
    TeacherSerializer,
    TutorSerializer,
    User,
    UserSerializer,
)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
