from rest_framework import serializers

from .models import StudentGroup, Subject, Speciality


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "semester")
        read_only_fields = ("id",)


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ("id", "name")
        read_only_fields = ("id",)


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("id", "name", "speciality", "quantity")
        read_only_fields = ("id",)
