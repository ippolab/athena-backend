from rest_framework import serializers

from .models import Student, Teacher, Tutor
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['username'] = user.username
        token['roles'] = [group.name.lower() for group in user.groups.all()]
        return token


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
