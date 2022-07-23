from rest_framework import permissions


class UserMePermission(permissions.BasePermission):
    message = 'Отказано в доступе!'

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated and obj.user == request.user)


class CategoriesGenresPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and request.user.role == "admin"
            or request.user.is_superuser)


class TitlesPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.method in permissions.SAFE_METHODS
            or (request.user.role == "admin" or request.user.is_superuser)
        )


class ReviewsCommentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and (request.method == 'Get')
            or (request.method == 'Post' and request.user.is_authenticated)
            or (request.method in ('Patch', 'Delete') and (
                obj.user == request.user
                or request.user.role in ("admin", "moderator")
                or request.user.is_superuser))
        )
