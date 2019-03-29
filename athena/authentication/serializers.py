from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer

from athena.authentication.models import User
from .models import Student, Teacher, Tutor


class RolesTokenObtainSlidingSerializer(TokenObtainSlidingSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token["username"] = user.username
        token["roles"] = [role.name.lower() for role in user.roles.all()]
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "second_name", "last_name", "roles")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("user", "cipher", "student_group",)


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ("user",)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("user", "subjects",)
