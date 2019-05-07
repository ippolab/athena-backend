import datetime

from django.db.models import DateField
from django.utils import timezone
from rest_framework import serializers

from athena.authentication.models import Student
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
            "subject",
            "student_group",
        )
        read_only_fields = ("id",)

    def validate_deadline(self, value: DateField):
        """
        Check that the student has group.
        """
        if value <= datetime.datetime.today():
            raise serializers.ValidationError("Deadline cant be <= today")
        return value


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class ReportInCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("name", "file", "attachment", "task", "student")

    def validate_student(self, value: Student):
        """
        Check that the student has group.
        """
        if not value.student_group:
            raise serializers.ValidationError("Student has not group")
        return value


class ReportInTutorRequestSerializer(serializers.ModelSerializer):
    checked_at = serializers.DateTimeField(default=timezone.now, read_only=True)

    class Meta:
        model = Report
        fields = ("status", "comment", "verified_by")


class ReportInStudentRequestSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(default=timezone.now, read_only=True)

    class Meta:
        model = Report
        fields = ("name", "file", "attachment")
