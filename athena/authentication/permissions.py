from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from rest_framework.request import Request


def _is_auth(request: Request) -> bool:
    return request.user and request.user.is_authenticated


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return _is_auth(request) and request.user.is_admin


class IsTutor(permissions.BasePermission):
    def has_permission(self, request: Request, _view):
        return _is_auth(request) and request.user.is_tutor


class IsStudent(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return _is_auth(request) and request.user.is_student


class IsStudentAndReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return (
                _is_auth(request)
                and request.user.is_student
                and request.method in SAFE_METHODS
        )


class IsStudentAndOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
                _is_auth(request)
                and request.user.is_student
                and obj.student == request.user
        )


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return _is_auth(request) and request.user.is_teacher
