from rest_framework import viewsets

from .models import Student, Teacher, Tutor
from .serializers import (
    StudentSerializer,
    TeacherSerializer,
    TutorSerializer,
)
from rest_framework_simplejwt.views import TokenObtainSlidingView
from .serializers import RolesTokenObtainSlidingSerializer


class RolesTokenObtainSlidingView(TokenObtainSlidingView):
    serializer_class = RolesTokenObtainSlidingSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
