from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainSlidingView

from .models import Student, Teacher, Tutor, User, Role
from .serializers import TokenSerializer, StudentSerializer, TeacherSerializer, TutorSerializer, UserSerializer, \
    RoleSerializer


class TokenView(TokenObtainSlidingView):
    serializer_class = TokenSerializer


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


@api_view(('GET',))
def get_profile_view(request: Request):
    serializer = UserSerializer(request.user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
