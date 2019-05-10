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


class IsOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return (
                _is_auth(request)
                and view.kwargs["id"] == request.user.id
        )


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return _is_auth(request) and request.user.is_teacher


class IsNotListAction(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return (
                _is_auth(request)
                and not view.action == "list"
        )
