from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainSlidingView

from .models import Role, Student, Teacher, Tutor, User
from .permissions import UserIsAdmin
from .serializers import (
    RoleSerializer,
    StudentSerializer,
    TeacherSerializer,
    TokenSerializer,
    TutorSerializer,
    UserInCreateSerializer,
    UserInResponseSerializer,
)


class TokenView(TokenObtainSlidingView):
    serializer_class = TokenSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInResponseSerializer
    permission_classes = (UserIsAdmin,)

    def create(self, request, **kwargs):
        serializer = UserInCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


@swagger_auto_schema(
    method="get",
    operation_summary="Get Current User Profile",
    operation_description="Retrieve profile for user that makes request",
    responses={200: UserInResponseSerializer},
)
@api_view(("GET",))
def get_profile_view(request: Request):
    serializer = UserInResponseSerializer(request.user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
