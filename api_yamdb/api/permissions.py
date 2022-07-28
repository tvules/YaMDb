from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """
    Разрешение, предоставляющее доступ
    только если метод запроса является безопасным(чтение).
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):
    """Разрешение, предоставляющее доступ только админу и суперюзеру."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_admin
        )


class IsStaff(permissions.BasePermission):
    """
    Разрешение на уровне объекта, предоставляющее доступ только персоналу.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user.is_superuser
            or request.user.is_admin
            or request.user.is_moderator
        )


class IsAuthorOrStaff(IsStaff):
    """
    Разрешение на уровне объекта,
    предоставляющее доступ только автору и персоналу.
    """

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return super().has_object_permission(request, view, obj)
