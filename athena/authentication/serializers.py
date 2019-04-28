from rest_framework import serializers

from .models import Role, Student, Teacher, Tutor, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("name",)


class UserInResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "second_name", "last_name", "roles")
        read_only_fields = ("id",)


class UserInCreateSerializer(UserInResponseSerializer):
    class Meta(UserInResponseSerializer.Meta):
        fields = UserInResponseSerializer.Meta.fields + ("password",)
        extra_kwargs = {"password": {"write_only": True}}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "cipher", "student_group")
        read_only_fields = ("id",)


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ("id",)
        read_only_fields = ("id",)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "subjects")
        read_only_fields = ("id",)
