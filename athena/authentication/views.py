from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainSlidingView

from .models import Student, Teacher, Tutor, User, Role
from .serializers import (
    RolesTokenObtainSlidingSerializer,
    StudentSerializer,
    TeacherSerializer,
    TutorSerializer,
    UserSerializer,
    RoleSerializer)


class RolesTokenObtainSlidingView(TokenObtainSlidingView):
    serializer_class = RolesTokenObtainSlidingSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


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
