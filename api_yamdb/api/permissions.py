from rest_framework import permissions


class UserMePermission(permissions.BasePermission):
    message = 'Отказано в доступе!'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.method in permissions.SAFE_METHODS
                or request.method == 'PATCH')
        )
