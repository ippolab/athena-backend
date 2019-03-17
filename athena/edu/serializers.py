from rest_framework import serializers

from .models import StudentGroup, Subject


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "url", "name")


class StudentGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("id", "url", "name", "quantity")
