from rest_framework import serializers

from .models import Report, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "theme",
            "description",
            "templates",
            "subject",
            "groups",
            "deadline",
        )
        read_only_fields = ("id",)


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "id",
            "title",
            "document",
            "attachment",
            "status",
            "checked",
            "task",
            "student",
        )
        read_only_fields = ("id",)
