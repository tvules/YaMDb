from rest_framework import permissions


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
