from rest_framework import serializers

from .models import StudentGroup, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name")
        read_only_fields = ("id",)


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("id", "name", "quantity")
        read_only_fields = ("id",)
