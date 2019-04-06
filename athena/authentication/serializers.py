from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer

from .models import User, Student, Teacher, Tutor, Role


class RolesTokenObtainSlidingSerializer(TokenObtainSlidingSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["username"] = user.username
        token["roles"] = [str(role).lower() for role in user.roles.all()]
        return token


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("name",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "second_name", "last_name", "roles")
        read_only_fields = ("id",)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "user", "cipher", "student_group",)
        read_only_fields = ("id",)


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ("id", "user",)
        read_only_fields = ("id",)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "user", "subjects",)
        read_only_fields = ("id",)
