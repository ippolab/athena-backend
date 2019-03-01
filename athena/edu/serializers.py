from rest_framework import serializers

from .models import StudentGroup, Subject


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ("url", "name")


class StudentGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("url", "name")
