from rest_framework import permissions


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


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта,
    позволяющее редактировать его только владельцам объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта,
    позволяющее редактировать его только персоналу.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_staff
        )


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (request.user.role == 'admin' or request.user.is_superuser)
            )
        )
