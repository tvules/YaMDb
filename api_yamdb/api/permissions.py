from rest_framework import permissions


class UserMePermission(permissions.BasePermission):
    message = 'Отказано в доступе!'

    def has_permission(self, request, view):
        return (request.user.is_authenticated)


class IsModeratorOrReadOnly(permissions.BasePermission):
    message = 'Отказано в доступе!'

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == 'moderator'
        )


class IsAdminPermission(permissions.BasePermission):
    message = 'Отказано в доступе!'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.role == 'admin' or request.user.is_superuser))
