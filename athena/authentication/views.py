from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainSlidingView

from .models import Role, Student, Teacher, Tutor, User
from .permissions import IsAdmin
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


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (IsAdmin,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserInResponseSerializer
    permission_classes = (IsAdmin,)

    def create(self, request, **kwargs):
        serializer = UserInCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        user = User.objects.create_user(**data)

        return Response(
            data=UserInResponseSerializer(user).data, status=status.HTTP_201_CREATED
        )


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet,
                     ):
    pass


class StudentViewSet(ProfileViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAdmin,)


class TutorViewSet(ProfileViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = (IsAdmin,)


class TeacherViewSet(ProfileViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdmin,)


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
