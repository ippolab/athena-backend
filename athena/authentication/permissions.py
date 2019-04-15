from rest_framework import permissions
from rest_framework.request import Request


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_admin


class IsTutor(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_tutor


class IsStudent(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_student


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_teacher
