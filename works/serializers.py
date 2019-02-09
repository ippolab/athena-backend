from rest_framework import serializers

from works.models import Task, Report


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'theme', 'description', 'templates', 'subject', 'groups', 'deadline')


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('url', 'title', 'document', 'attachment', 'status', 'checked', 'task', 'student')
