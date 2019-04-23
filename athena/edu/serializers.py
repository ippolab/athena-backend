from rest_framework import serializers

from .models import Speciality, StudentGroup, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "semester")
        read_only_fields = ("id",)


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ("id", "name", "cipher")
        read_only_fields = ("id",)


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("id", "name", "speciality")
        read_only_fields = ("id",)
