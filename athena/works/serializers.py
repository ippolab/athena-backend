from rest_framework import serializers

from .models import Report, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "file",
            "attachment",
            "deadline",
            "create_datetime",
            "edit_datetime",
            "subject",
            "student_group",
        )
        read_only_fields = ("id", "create_datetime", "edit_datetime")


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            "id",
            "name",
            "file",
            "attachment",
            "status",
            "create_datetime",
            "edit_datetime",
            "comment",
            "task",
            "student",
            "tutor",
            "teacher",
        )
        read_only_fields = ("id", "create_datetime", "edit_datetime")
