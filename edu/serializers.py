from rest_framework import serializers

from edu.models import Subject, StudentGroup


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'name', 'teacher_id')


class StudentGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('url', 'name', 'student_id',)
