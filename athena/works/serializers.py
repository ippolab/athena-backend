import datetime

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

    def validate_name(self, value: str):
        return value.strip()

    def validate_deadline(self, value):
        if value <= datetime.date.today():
            raise serializers.ValidationError("Deadline cant be <= today")
        return value


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
        read_only_fields = ("id",)

    def validate_student(self, value: Student):
        """
        Check that the student has group and cipher.
        """
        if not value.student_group:
            raise serializers.ValidationError("Student has not group")
        if not value.cipher:
            raise serializers.ValidationError("Student has not cipher")
        return value


class ReportInCreateSerializer(ReportSerializer):
    class Meta(ReportSerializer.Meta):
        fields = ("id", "task", "name", "file", "attachment", "student")
        extra_kwargs = {"name": {"default": ""}}
        order_by = ("task", "student", "name")

    # def validate_name(self, value: str): todo set task.name
    #     if value.strip() == "":
    #         return self.instance.task.name #None


class ReportInTutorRequestSerializer(serializers.ModelSerializer):
    checked_at = serializers.HiddenField(default=timezone.now)
    verified_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta(ReportSerializer.Meta):
        fields = ("status", "comment", "verified_by", "checked_at")


class ReportInStudentRequestSerializer(serializers.ModelSerializer):
    updated_at = serializers.HiddenField(default=timezone.now)

    class Meta(ReportSerializer.Meta):
        fields = ("name", "file", "attachment", "updated_at")
